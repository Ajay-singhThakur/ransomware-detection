# AI-Powered Ransomware Detection (Full Project)

## What this repo contains
- `backend/` : Flask backend, ML training, contract ABI folder
- `blockchain/` : Hardhat project & deploy scripts
- `frontend/` : React app with toast notifications
- `docker-compose.yml` : brings up backend + frontend + IPFS (not hardhat)

## Quick steps (recommended)
1. Install Node (>=18) and Python (3.10+).
2. Start a local Hardhat node and deploy contract:
   ```bash
   cd blockchain
   npm install
   npx hardhat node
   # in another terminal:
   npx hardhat run scripts/deploy_and_copy.js --network localhost
