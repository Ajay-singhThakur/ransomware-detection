import os
import json
import hashlib
import joblib
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from web3 import Web3

from detector import model_utils

load_dotenv()

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Model
MODEL_PATH = os.path.join(BASE_DIR, "detector", "model.joblib")
model = joblib.load(MODEL_PATH) if os.path.exists(MODEL_PATH) else None

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Blockchain & ABI
RPC_URL = os.getenv("BLOCKCHAIN_RPC", "http://127.0.0.1:8545")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS") or None
PRIVATE_KEY = os.getenv("PRIVATE_KEY") or None
ABI_PATH = os.path.join(BASE_DIR, "contracts_meta", "RansomwareStorage.json")
DEPLOYED_ADDRESS_PATH = os.path.join(BASE_DIR, "contracts_meta", "deployed_address.txt")

w3 = Web3(Web3.HTTPProvider(RPC_URL))

contract = None
if os.path.exists(ABI_PATH):
    with open(ABI_PATH, "r") as f:
        contract_abi = json.load(f)
    # prefer explicit env CONTRACT_ADDRESS else file
    if CONTRACT_ADDRESS and Web3.is_address(CONTRACT_ADDRESS):
        contract_address = Web3.to_checksum_address(CONTRACT_ADDRESS)
    elif os.path.exists(DEPLOYED_ADDRESS_PATH):
        addr = open(DEPLOYED_ADDRESS_PATH).read().strip()
        contract_address = Web3.to_checksum_address(addr) if Web3.is_address(addr) else None
    else:
        contract_address = None

    if contract_address:
        contract = w3.eth.contract(address=contract_address, abi=contract_abi)

account = None
if PRIVATE_KEY:
    account = w3.eth.account.from_key(PRIVATE_KEY)


@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Extract features and predict
    features = model_utils.extract_features(filepath)
    prediction = model.predict([features])[0] if model else "Unknown"

    file_hash = hashlib.sha256(open(filepath, "rb").read()).hexdigest()

    # Optional: add to IPFS if ipfs/http client available (not mandatory)
    ipfs_hash = None
    try:
        import ipfshttpclient
        client = ipfshttpclient.connect('/dns/host.docker.internal/tcp/5001/http')
        ipfs_res = client.add(filepath)
        ipfs_hash = ipfs_res.get("Hash")
    except Exception:
        # fallback: ignore IPFS upload if not configured
        ipfs_hash = None

    # Optional: record on blockchain
    tx_status = None
    if contract and account:
        try:
            nonce = w3.eth.get_transaction_count(account.address)
            tx = contract.functions.storeFileEvent(file.filename, ipfs_hash or "", str(prediction)).build_transaction({
                "from": account.address,
                "nonce": nonce,
                "gas": 500000,
                "gasPrice": w3.to_wei("10", "gwei")
            })
            signed = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
            tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
            receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
            tx_status = "Success" if receipt.get("status") == 1 else "Failed"
        except Exception as e:
            tx_status = f"error: {str(e)}"

    return jsonify({
        "filename": file.filename,
        "prediction": str(prediction),
        "sha256": file_hash,
        "ipfs_hash": ipfs_hash,
        "blockchain_tx": tx_status
    })


if __name__ == "__main__":
    # use host 0.0.0.0 so docker maps port correctly
    app.run(host="0.0.0.0", port=5000)
