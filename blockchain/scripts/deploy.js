// scripts/deploy.js
const fs = require("fs");
const path = require("path");

async function main() {
  const RansomwareStorage = await ethers.getContractFactory("RansomwareStorage");
  console.log("🚀 Deploying RansomwareStorage contract...");
  const ransomwareStorage = await RansomwareStorage.deploy();
  await ransomwareStorage.deployed();

  console.log("✅ Deployed at:", ransomwareStorage.address);

  // Get ABI from artifacts
  const artifactPath = path.join(__dirname, "../artifacts/contracts/RansomwareStorage.sol/RansomwareStorage.json");
  const artifact = JSON.parse(fs.readFileSync(artifactPath, "utf8"));

  // Create folder to store ABI and address
  const outputDir = path.join(__dirname, "../contracts_meta");
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir);
  }

  // Save ABI and contract address
  fs.writeFileSync(
    path.join(outputDir, "RansomwareStorageABI.json"),
    JSON.stringify(artifact.abi, null, 2)
  );

  fs.writeFileSync(
    path.join(outputDir, "deployed_address.txt"),
    ransomwareStorage.address
  );

  console.log("📁 ABI and address saved inside /contracts_meta/");
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
