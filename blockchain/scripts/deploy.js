cat > blockchain/scripts/deploy.js <<'EOF'
const hre = require("hardhat");
const fs = require("fs");
const path = require("path");

async function main() {
  const FileRegistry = await hre.ethers.getContractFactory("FileRegistry");
  const registry = await FileRegistry.deploy();
  await registry.deployed();
  console.log("FileRegistry deployed to:", registry.address);

  // write ABI & address for backend
  const outDir = path.resolve(__dirname, '../../contracts_meta');
  if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });

  const abi = registry.interface.format('json');
  fs.writeFileSync(path.join(outDir, 'FileRegistryABI.json'), JSON.stringify(JSON.parse(abi), null, 2));
  fs.writeFileSync(path.join(outDir, 'deployed_address.txt'), registry.address);
  console.log("Saved ABI and address to", outDir);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
EOF
