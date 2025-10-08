#!/bin/bash
# Run from repo root. Requires node + hardhat installed.
cd blockchain || exit
npm install
# run hardhat node in separate terminal first: npx hardhat node
npx hardhat run scripts/deploy_and_copy.js --network localhost
echo "ABI and address should be copied to backend/contracts_meta/"
#!/bin/bash
echo "🚀 Setting up Ransomware Detection Project..."

# Create backend venv
cd backend
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
deactivate
cd ..

# Build Docker containers
docker-compose build

echo "✅ Setup complete. Run 'docker-compose up' to start the project."
