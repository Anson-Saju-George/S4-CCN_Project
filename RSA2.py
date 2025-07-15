from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import socket

def generate_key_pair(filename):
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    with open(filename + '_private.pem', 'wb') as f:
        f.write(private_key)
    with open(filename + '_public.pem', 'wb') as f:
        f.write(public_key)

def encrypt_message(message, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    return cipher.encrypt(message.encode())

def decrypt_message(encrypted_message, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    return cipher.decrypt(encrypted_message)

def main():
    # Generate or load key pair
    generate_key_pair('shared_key')

    # Load key pair
    private_key = RSA.import_key(open('shared_key_private.pem').read())
    public_key = RSA.import_key(open('shared_key_public.pem').read())

    # Set up socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 8000))

    # Send encrypted message and receive response
    while True:
        message = input("Enter your message: ")
        encrypted_message = encrypt_message(message, public_key)
        client_socket.send(encrypted_message)

        # Receive response
        response = client_socket.recv(1024)
        decrypted_response = decrypt_message(response, private_key)
        print("Server:", decrypted_response.decode())

    client_socket.close()

if __name__ == "__main__":
    main()
