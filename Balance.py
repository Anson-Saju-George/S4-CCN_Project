from web3 import Web3

# Connect to Ganache (replace 'http://127.0.0.1:7545' with the RPC server URL provided by Ganache)
ganache_url = 'http://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Check connection
if web3.is_connected():
    print('Connected to Ganache')
else:
    print('Failed to connect to Ganache')
    exit()

# Ethereum account address to check balance (replace with your Ethereum account address)
account_address = '0xBe57a0BF1d71fED306E393A1d7e0F365843988E5'

# Get account balance
balance_wei = web3.eth.get_balance(account_address)

# Convert balance from Wei to Ether
balance_eth = web3.from_wei(balance_wei, 'ether')

print(f'Balance of {account_address}: {balance_eth} ETH')
