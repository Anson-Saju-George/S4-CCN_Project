from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import socket

# Function to encrypt a message using a public key
def encrypt_message(message, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    return cipher.encrypt(message.encode())

# Function to decrypt a message using a private key
def decrypt_message(encrypted_message, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message.decode()

# Function for Client A
def client_a():
    # Load keys
    private_key = RSA.import_key(open('C://Users//HP-OMEN//OneDrive//Desktop//CCN_Project//shared_private.pem').read())
    public_key = RSA.import_key(open('C://Users//HP-OMEN//OneDrive//Desktop//CCN_Project//shared_public.pem').read())

    # Set up socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 8000))

    # Send encrypted message to Client B and receive response
    while True:
        message = input("Client A - Enter your message: ")
        encrypted_message = encrypt_message(message, public_key)
        client_socket.send(encrypted_message)

        # Receive response from Client B
        response = client_socket.recv(1024)
        decrypted_response = decrypt_message(response, private_key)
        print("Client B:", decrypted_response)

    client_socket.close()

# Function for Client B
def client_b():
    # Load keys
    private_key = RSA.import_key(open('C://Users//HP-OMEN//OneDrive//Desktop//CCN_Project//shared_private.pem').read())
    public_key = RSA.import_key(open('C://Users//HP-OMEN//OneDrive//Desktop//CCN_Project//shared_public.pem').read())

    # Set up socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 8000))

    # Send encrypted message to Client A and receive response
    while True:
        message = input("Client B - Enter your message: ")
        encrypted_message = encrypt_message(message, public_key)
        client_socket.send(encrypted_message)

        # Receive response from Client A
        response = client_socket.recv(1024)
        decrypted_response = decrypt_message(response, private_key)
        print("Client A:", decrypted_response)

    client_socket.close()

# Main function
def main():
    # Start Client A and Client B
    client_a()
    client_b()
C://Users//HP-OMEN//OneDrive//Desktop//CCN_Project//
if __name__ == "__main__":
    main()
