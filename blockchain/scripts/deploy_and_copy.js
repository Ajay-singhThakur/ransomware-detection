const fs = require("fs");
const path = require("path");
const hre = require("hardhat");

async function main() {
  const ContractFactory = await hre.ethers.getContractFactory("RansomwareStorage");
  const contract = await ContractFactory.deploy();
  await contract.deployed();
  console.log("Deployed RansomwareStorage at:", contract.address);

  // write artifact (abi) and deployed address to backend/contracts_meta
  const backendMetaDir = path.join(__dirname, "..", "..", "backend", "contracts_meta");
  if (!fs.existsSync(backendMetaDir)) fs.mkdirSync(backendMetaDir, { recursive: true });

  const artifact = await hre.artifacts.readArtifact("RansomwareStorage");
  fs.writeFileSync(path.join(backendMetaDir, "RansomwareStorage.json"), JSON.stringify(artifact, null, 2));
  fs.writeFileSync(path.join(backendMetaDir, "deployed_address.txt"), contract.address);

  console.log("ABI and address copied to backend/contracts_meta/");
}

main().catch((err) => {
  console.error(err);
  process.exitCode = 1;
});
