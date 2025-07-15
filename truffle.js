module.exports = {
  // Configure your networks here
networks: {
    // Ganache local blockchain
    development: {
        host: "127.0.0.1",
        port: 7545,
        network_id: "*", // Match any network id
    },
    // Additional networks can be added here for different environments
    // For example, Rinkeby test network
    rinkeby: {
        host: "localhost",
        port: 7545,
        network_id: 4,
      gas: 6000000, // Gas limit used for deploys
    },
    // Add more network configurations as needed
},
  // Configure compiler settings
compilers: {
    solc: {
    version: "0.8.0", // Specify compiler version
    settings: {
        optimizer: {
        enabled: true,
        runs: 200,
    },
    },
},
},
};
