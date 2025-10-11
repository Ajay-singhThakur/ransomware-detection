import json
import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

BLOCKCHAIN_RPC_URL = os.getenv("BLOCKCHAIN_RPC_URL", "http://blockchain-node:8545")
META_PATH = "/app/contracts_meta/"
ABI_PATH = os.path.join(META_PATH, "RansomwareStorageABI.json")
ADDRESS_PATH = os.path.join(META_PATH, "deployed_address.txt")

w3 = Web3(Web3.HTTPProvider(BLOCKCHAIN_RPC_URL))
w3.eth.default_account = w3.eth.accounts[0]

def get_contract():
    try:
        with open(ABI_PATH, 'r') as f:
            contract_abi = json.load(f)
        with open(ADDRESS_PATH, 'r') as f:
            contract_address = f.read().strip()
    except FileNotFoundError:
        print("❌ ABI or contract address not found. Make sure the blockchain node has deployed it.")
        return None
    return w3.eth.contract(address=contract_address, abi=contract_abi)

contract = get_contract()

def log_file_to_blockchain(file_name, file_hash, ipfs_cid, detection_result):
    if not contract:
        raise ConnectionError("Smart contract not initialized.")
    try:
        tx_hash = contract.functions.addFileRecord(
            file_name,
            file_hash,
            ipfs_cid,
            detection_result
        ).transact()
        w3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Transaction successful with hash: {tx_hash.hex()}")
        return tx_hash.hex()
    except Exception as e:
        print(f"Error sending transaction to blockchain: {e}")
        return None