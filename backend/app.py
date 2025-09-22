cat > backend/app.py <<'EOF'
import os, json, time
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import ipfshttpclient
from detector.model_utils import predict_file
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

UPLOAD_DIR = '/app/uploads'
os.makedirs(UPLOAD_DIR, exist_ok=True)

IPFS_API = os.getenv("IPFS_API","/dns/ipfs/tcp/5001/http")
GANACHE_RPC = os.getenv("GANACHE_RPC","http://ganache:8545")
CONTRACT_ABI_PATH = '/app/contracts_meta/FileRegistryABI.json'
CONTRACT_ADDR_PATH = '/app/contracts_meta/deployed_address.txt'

app = Flask(__name__)

# Web3 setup (connect to ganache service)
w3 = Web3(Web3.HTTPProvider(GANACHE_RPC))

def load_contract():
    if not os.path.exists(CONTRACT_ABI_PATH) or not os.path.exists(CONTRACT_ADDR_PATH):
        return None
    with open(CONTRACT_ABI_PATH, 'r') as f:
        abi = json.load(f)
    with open(CONTRACT_ADDR_PATH, 'r') as f:
        addr = f.read().strip()
    try:
        return w3.eth.contract(address=w3.toChecksumAddress(addr), abi=abi)
    except Exception:
        return None

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "no file uploaded"}), 400
    f = request.files['file']
    fname = secure_filename(f.filename)
    if fname == '':
        return jsonify({"error": "empty filename"}), 400
    dst = os.path.join(UPLOAD_DIR, fname)
    f.save(dst)

    # run ML detector
    res = predict_file(dst)  # returns pred, score, entropy, size_kb
    if res["pred"] == 1:
        # flagged as malicious
        return jsonify({"status":"quarantined", "score":res["score"], "entropy":res["entropy"], "size_kb":res["size_kb"]}), 200

    # safe: add to IPFS
    try:
        client = ipfshttpclient.connect(IPFS_API)
        add_res = client.add(dst)
        cid = add_res['Hash']
    except Exception as e:
        return jsonify({"status":"error", "message":"IPFS add failed: " + str(e)}), 500

    # best-effort try to register on-chain
    chain_result = {"registered": False, "reason": "contract missing"}
    contract = load_contract()
    if contract is not None and w3.isConnected():
        try:
            # use first Ganache account (unlocked)
            acct = w3.eth.accounts[0]
            tx = contract.functions.uploadFile(cid).transact({"from": acct})
            receipt = w3.eth.wait_for_transaction_receipt(tx)
            chain_result = {"registered": True, "tx": receipt.transactionHash.hex()}
        except Exception as e:
            chain_result = {"registered": False, "reason": str(e)}

    return jsonify({
        "status":"ok",
        "cid": cid,
        "ml": res,
        "chain": chain_result
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
EOF
