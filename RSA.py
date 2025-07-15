from Crypto.PublicKey import RSA

def generate_rsa_key_pair(filename):
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    with open(f"{filename}_private.pem", "wb") as private_file:
        private_file.write(private_key)
    with open(f"{filename}_public.pem", "wb") as public_file:
        public_file.write(public_key)

# Generate server's RSA key pair
generate_rsa_key_pair("server")

# Generate client's RSA key pair
generate_rsa_key_pair("client")
