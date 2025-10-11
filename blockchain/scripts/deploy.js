const hre = require("hardhat");
const fs = require("fs");
const path = require("path");

async function main() {
  const Contract = await hre.ethers.getContractFactory("RansomwareStorage");
  const contract = await Contract.deploy();

  await contract.deployed();

  console.log(`RansomwareStorage contract deployed to: ${contract.address}`);

  // ---- EXPORT ARTIFACTS ----
  const contractsMetaDir = path.join(__dirname, "..", "contracts_meta");

  if (!fs.existsSync(contractsMetaDir)) {
    fs.mkdirSync(contractsMetaDir);
  }

  // 1. Export the contract address
  fs.writeFileSync(
    path.join(contractsMetaDir, "deployed_address.txt"),
    contract.address
  );

  // 2. Export the contract ABI
  const contractArtifact = hre.artifacts.readArtifactSync("RansomwareStorage");
  fs.writeFileSync(
    path.join(contractsMetaDir, "RansomwareStorageABI.json"),
    JSON.stringify(contractArtifact.abi, null, 2)
  );

  console.log("✅ Contract address and ABI exported to contracts_meta/");
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});