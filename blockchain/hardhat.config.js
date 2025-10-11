require("@nomicfoundation/hardhat-toolbox");
require("dotenv").config();

// This is a sample Hardhat task. To learn how to create your own go to
// https://hardhat.org/guides/create-task.html
task("accounts", "Prints the list of accounts", async (taskArgs, hre) => {
  const accounts = await hre.ethers.getSigners();

  for (const account of accounts) {
    console.log(account.address);
  }
});

// Immediately run deployment script after node starts
// We achieve this by overriding the `node` task
task("node", "Starts a JSON-RPC server on top of Hardhat Network", async function (args, hre, runSuper) {
  // First, run the original `node` task in the background
  const nodePromise = runSuper(args);
  
  // Wait a bit for the node to be ready
  await new Promise(resolve => setTimeout(resolve, 2000));
  
  // Run our deployment script
  console.log("🚀 Deploying contracts...");
  await hre.run("run", { script: "scripts/deploy.js" });
  console.log("✅ Contracts deployed.");
  
  // Keep the node running
  await nodePromise;
});


/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: "0.8.17",
  networks: {
    hardhat: {
      chainId: 1337, // Standard for local networks
    },
  },
};