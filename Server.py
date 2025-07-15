from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import socket

def decrypt_message(encrypted_message, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    return cipher.decrypt(encrypted_message)

def main():
    # Load server's private key
    server_private_key = RSA.import_key(open('C:\\Users\\HP-OMEN\\OneDrive\\Desktop\\CCN_Project\\server_private.pem').read())

    # Set up server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(5)
    print("Server is listening...")

    # Accept client connection
    client_socket, address = server_socket.accept()
    print(f"Connection from {address} has been established.")

    # Receive encrypted message from client and decrypt it
    while True:
        encrypted_message = client_socket.recv(1024)
        if not encrypted_message:
            break
        decrypted_message = decrypt_message(encrypted_message, server_private_key)
        print("Client:", decrypted_message.decode())

        # Send response to client
        message = input("Enter your message: ")
        client_socket.send(message.encode())

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
