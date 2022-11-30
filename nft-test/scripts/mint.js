// We require the Hardhat Runtime Environment explicitly here. This is optional
// but useful for running the script in a standalone fashion through `node <script>`.
//
// You can also run a script with `npx hardhat run <script>`. If you do that, Hardhat
// will compile your contracts, add the Hardhat Runtime Environment's members to the
// global scope, and execute the script.
const hre = require("hardhat");

async function main() {

  const NFTEvent = await hre.ethers.getContractFactory("MyNFT");
  const nFTevent = await NFTEvent.attach("0xf3f74442fde851e6849f8fe9a98649d7e60c3922");

  await nFTevent.mintNFT("0x44Dc68892A17ea60E98dB3194AE8667DDDeC6900", "https://gateway.pinata.cloud/ipfs/QmSFfXdM5EdXkMA5ipxsZPWQNarLPdCafXEZFdLyeS37FY");

  console.log(
    ` deployed to ${nFTevent.address}`
  );
}

// We recommend this pattern to be able to use async/await everywhere
// and properly handle errors.
main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});