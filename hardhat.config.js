require("@nomicfoundation/hardhat-toolbox");


module.exports = {
  solidity: "0.8.17",
  networks: {
    mumbai: {
      url: "https://polygon-mumbai.g.alchemy.com/v2/xPACxJYzW3ovyVZS_NMuOHO-BZaKcF2d",
      accounts:['3793d6cfddc42525668088ed09bc23b119da00cecf2567e82572a05e3a1774a7'
      ],
    },
  },
};