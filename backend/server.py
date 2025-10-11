import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Import routes
from routes.file_routes import file_bp
from routes.auth_routes import auth_bp # <-- ADD THIS LINE

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

# Register Blueprints
app.register_blueprint(file_bp, url_prefix='/api')
app.register_blueprint(auth_bp, url_prefix='/api/auth') # <-- ADD THIS LINE

@app.route("/")
def index():
    return "<h1>Backend is running!</h1>"

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=os.environ.get('FLASK_DEBUG') == '1')