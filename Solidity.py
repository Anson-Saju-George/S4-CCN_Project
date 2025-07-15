from web3 import Web3
from solcx import compile_source

# Connect to local Ethereum node
web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

# Solidity source code
contract_source_code = '''
pragma solidity ^0.8.0;

contract SimpleStorage {
    uint256 public storedData;

    function set(uint256 x) public {
        storedData = x;
    }

    function get() public view returns (uint256) {
        return storedData;
    }
}
'''

# Compile the Solidity code
compiled_sol = compile_source(contract_source_code)
contract_interface = compiled_sol['<stdin>:SimpleStorage']

# Deploy the contract
SimpleStorage = web3.eth.contract(
    abi=contract_interface['abi'],
    bytecode=contract_interface['bin']
)

tx_hash = SimpleStorage.constructor().transact()
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

contract_address = tx_receipt.contractAddress
