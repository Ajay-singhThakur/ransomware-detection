import ipfshttpclient
import os

try:
    # Use an IPFS client compatible with your Kubo version
    # The 'v0.8.0' you are using works with this library
    client = ipfshttpclient.connect('/dns/ipfs/tcp/5001')
    print("✅ Connected to IPFS node.")
except Exception as e:
    print(f"❌ Could not connect to IPFS daemon: {e}")
    client = None

def add_to_ipfs(file_path):
    """Adds a file to IPFS, copies it to MFS, and returns its CID."""
    if not client:
        raise ConnectionError("IPFS client is not connected.")
    
    try:
        # Step 1: Add the file to the main IPFS storage (the "library")
        res = client.add(file_path)
        cid = res['Hash']
        print(f"File {file_path} added to IPFS with CID: {cid}")

        # --- THIS IS THE NEW FIX ---
        # Step 2: Copy the file to the MFS (the "shelf")
        #         so it appears in the WebUI "Files" page.
        
        file_name = os.path.basename(file_path)
        mfs_path = f'/{file_name}' # The path on the "Files" page, e.g., "/resume.pdf"
        
        try:
            # Copy the file (using its CID) to the MFS path
            client.files.cp(f'/ipfs/{cid}', mfs_path, parents=True)
            print(f"File copied to MFS at: {mfs_path}")
        except Exception as e:
            # If the file already exists, it might throw an error.
            # We log it as a warning but don't crash.
            print(f"Warning: Could not copy file to MFS. Error: {e}")
        # --- END OF FIX ---

        return cid # Return the CID

    except Exception as e:
        print(f"Error adding file to IPFS: {e}")
        return None

def list_files_in_mfs():
    """Lists all files in the root of the IPFS MFS."""
    if not client:
        raise ConnectionError("IPFS client is not connected.")
    
    try:
        # List the contents of the MFS root directory
        response = client.files.ls('/', l=True)
        files = response.get('Entries', [])
        return files
    except Exception as e:
        print(f"Error listing MFS files: {e}")
        return []