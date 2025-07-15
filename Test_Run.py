from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import hashlib

# Function to encrypt a message using AES
def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    cipher_text = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher_text, cipher.iv

# Function to decrypt a message using AES
def decrypt_message(cipher_text, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    message = unpad(cipher.decrypt(cipher_text), AES.block_size).decode()
    return message

# Function to sign a message using Ethereum account private key
def sign_message(message, private_key):
    hashed_message = hashlib.sha256(message.encode()).digest()
    # Here you would usually use a library like Web3.py to sign the message using the private key
    # For demonstration, let's just return the hashed message
    return hashed_message.hex()

# Function to verify a signed message using Ethereum account address
def verify_message(message, signature, account_address):
    hashed_message = hashlib.sha256(message.encode()).digest()
    # Here you would usually use a library like Web3.py to verify the signature using the public key
    # For demonstration, let's just compare the hashed message with the signature
    return hashed_message.hex() == signature

# Sample message to send
message_to_send = "Hello, World!"

# Generate random AES key and IV
aes_key = get_random_bytes(16)
aes_iv = get_random_bytes(16)

# Encrypt the message
cipher_text, iv = encrypt_message(message_to_send, aes_key)

# Sign the message
signature = sign_message(message_to_send, "YOUR_PRIVATE_KEY_HERE")

# Verify the signature
is_verified = verify_message(message_to_send, signature, "YOUR_PUBLIC_ADDRESS_HERE")

# Decrypt the message
decrypted_message = decrypt_message(cipher_text, aes_key, iv)

# Output results
print("Original Message:", message_to_send)
print("Encrypted Message:", cipher_text.hex())
print("IV:", iv.hex())
print("Signature:", signature)
print("Signature Verified:", is_verified)
print("Decrypted Message:", decrypted_message)
