from web3 import Web3

# Sepolia network URL from Infura
infura_url = 'https://sepolia.infura.io/v3/32df86fc7ced4997a2644eb1800a250c'

# Initialize a Web3 instance
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check if the connection is successful
if web3.is_connected():
    print("Connected to the Sepolia network")
    # Get the latest block number
    block_number = web3.eth.block_number
    print(f"The latest block number is {block_number}")
else:
    print("Failed to connect to the Sepolia network")
