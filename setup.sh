#!/bin/bash

echo "🚀 Starting project setup..."

# Create necessary directories
echo "Creating directories..."
mkdir -p backend/model backend/routes backend/utils
mkdir -p blockchain/contracts blockchain/scripts blockchain/contracts_meta
mkdir -p frontend/src/components frontend/src/pages frontend/src/assets frontend/src/services
mkdir -p ipfs_data

# Create placeholder .env files
echo "Creating .env files..."
echo "FLASK_DEBUG=1" > backend/.env
echo "BLOCKCHAIN_RPC_URL=http://blockchain-node:8545" >> backend/.env

echo "VITE_API_BASE_URL=http://localhost:5000" > frontend/.env

# Create empty __init__.py files to make python packages
touch backend/__init__.py
touch backend/routes/__init__.py
touch backend/utils/__init__.py

echo "✅ Setup complete! You can now run 'docker-compose up --build'."