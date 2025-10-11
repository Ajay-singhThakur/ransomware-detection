from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth_routes', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    # --- THIS IS A PLACEHOLDER ---
    # A real implementation would:
    # 1. Get username, email, password from request.json
    # 2. Hash the password
    # 3. Save the new user to a database
    # 4. Return a success message or token
    print("Received registration attempt.")
    return jsonify({"message": "User registration endpoint is not yet implemented."}), 501 # 501 means "Not Implemented"

@auth_bp.route('/login', methods=['POST'])
def login():
    # --- THIS IS A PLACEHOLDER ---
    # A real implementation would:
    # 1. Get email, password from request.json
    # 2. Find the user in the database
    # 3. Compare the hashed password
    # 4. Generate and return a JWT (JSON Web Token)
    print("Received login attempt.")
    return jsonify({"message": "User login endpoint is not yet implemented."}), 501