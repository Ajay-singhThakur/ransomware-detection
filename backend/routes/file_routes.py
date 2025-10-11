import os
import hashlib
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename

# Corrected, explicit imports
from utils.ipfs_utils import add_to_ipfs
from utils.ml_utils import predict_ransomware
from utils.blockchain_utils import log_file_to_blockchain

file_bp = Blueprint('file_routes', __name__)

UPLOAD_FOLDER = 'temp_uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@file_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        filename = secure_filename(file.filename)
        temp_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(temp_path)

        try:
            # 1. Perform ML analysis
            prediction = predict_ransomware(temp_path)

            # 2. Upload file to IPFS
            ipfs_cid = add_to_ipfs(temp_path)
            if not ipfs_cid:
                raise Exception("Failed to upload to IPFS.")

            # 3. Calculate file hash (SHA256)
            with open(temp_path, 'rb') as f:
                file_bytes = f.read()
                file_hash = hashlib.sha256(file_bytes).hexdigest()

            # 4. Log transaction to blockchain
            tx_hash = log_file_to_blockchain(
                file_name=filename,
                file_hash=file_hash,
                ipfs_cid=ipfs_cid,
                detection_result=prediction
            )
            if not tx_hash:
                raise Exception("Failed to log to blockchain.")

            os.remove(temp_path)

            return jsonify({
                "message": "File processed successfully!",
                "filename": filename,
                "ipfs_cid": ipfs_cid,
                "file_hash": file_hash,
                "ml_result": prediction,
                "blockchain_tx": tx_hash
            }), 200

        except Exception as e:
            if os.path.exists(temp_path):
                os.remove(temp_path)
            return jsonify({"error": str(e)}), 500

    return jsonify({"error": "File upload failed"}), 500