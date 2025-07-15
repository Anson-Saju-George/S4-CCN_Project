from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import socket

# Define key size
KEY_SIZE = 2048

# Function to encrypt a message using a public key
def encrypt_message(message, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

# Function to decrypt a message using a private key
def decrypt_message(encrypted_message, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message.decode()

def main():
    # Load private and public keys
    client_a_private_key = RSA.import_key(open('C://Users//HP-OMEN//OneDrive//Desktop//CCN_Project//client_a_private.pem').read())
    client_b_public_key = RSA.import_key(open('C://Users//HP-OMEN//OneDrive//Desktop//CCN_Project//client_b_public.pem').read())

    # Set up socket
    client_a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_a_socket.connect(('127.0.0.1', 8000))

    # Send and receive messages
    while True:
        # Client A sends a message
        message_a = input("Client A: ")
        encrypted_message_a = encrypt_message(message_a, client_b_public_key)
        client_a_socket.send(encrypted_message_a)

        # Client A receives and decrypts the message from Client B
        encrypted_message_b = client_a_socket.recv(1024)
        decrypted_message_b = decrypt_message(encrypted_message_b, client_a_private_key)
        print("Client B:", decrypted_message_b)

    client_a_socket.close()

if __name__ == "__main__":
    main()
