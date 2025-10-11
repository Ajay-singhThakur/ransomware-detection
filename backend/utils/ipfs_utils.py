import ipfshttpclient
import os

try:
    client = ipfshttpclient.connect('/dns/ipfs/tcp/5001')
    print("✅ Connected to IPFS node.")
except Exception as e:
    print(f"❌ Could not connect to IPFS daemon: {e}")
    client = None

def add_to_ipfs(file_path):
    if not client:
        raise ConnectionError("IPFS client is not connected.")
    try:
        res = client.add(file_path)
        print(f"File {file_path} added to IPFS with CID: {res['Hash']}")
        return res['Hash']
    except Exception as e:
        print(f"Error adding file to IPFS: {e}")
        return None