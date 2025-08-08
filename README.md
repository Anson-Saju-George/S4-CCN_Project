# S4-CCN_Project

This repository contains the source code and resources for my fourth semester Computer Communication Networks (CCN) project. The project demonstrates secure communication, blockchain integration, and network security concepts using Python, Solidity, and supporting tools.

## Project Overview

- **Secure Communication:** Implements RSA and AES encryption for secure messaging between clients and server.
- **Blockchain Integration:** Uses Ethereum smart contracts and Web3.py for blockchain-based operations and balance checks.
- **Network Security:** Includes a honeypot server and ARP spoofing detection using Scapy.

## File Structure & Description

### Cryptography & Secure Messaging
- `RSA.py`, `RSA2.py`: Scripts to generate RSA key pairs and demonstrate encryption/decryption.
- `ClientA.py`, `ClientB.py`, `Both.py`: Client-side scripts for secure message exchange using RSA keys.
- `Server.py`: Server-side script for receiving and decrypting messages from clients.
- `client_a_private.pem`, `client_a_public.pem`, `client_b_private.pem`, `client_b_public.pem`: RSA key files for clients.
- `Test_Run.py`: Demonstrates AES encryption/decryption and message signing/verification.

### Blockchain & Smart Contracts
- `Balance.py`: Checks Ethereum account balance using Web3.py and Ganache.
- `Solidity.py`: Compiles and deploys a simple Solidity smart contract using Web3.py and solcx.
- `run.py`: Installs the required Solidity compiler version.
- `truffle.js`: Truffle configuration for blockchain network and compiler settings.

### Network Security
- `1.py`: Honeypot server using Twisted to log incoming connections.
- `Spoof/A.py`: Detects ARP spoofing attacks using Scapy.

### Miscellaneous
- `tempCodeRunnerFile.py`: Temporary file, likely for code runner usage.

## How to Run

1. **Install Dependencies:**
   - Python packages: `pycryptodome`, `web3`, `solcx`, `scapy`, `twisted`
   - Node.js and Truffle for smart contract deployment
2. **Generate RSA Keys:**
   - Run `RSA.py` or `RSA2.py` to generate key pairs.
3. **Start Blockchain (Ganache):**
   - Ensure Ganache is running for blockchain-related scripts.
4. **Run Scripts:**
   - Use the respective Python scripts for secure messaging, blockchain operations, and network security demonstrations.

## Notes
- Update file paths in scripts as needed for your environment.
- Refer to each script for specific usage instructions and required arguments.

---
**Author:** Anson Saju George
**Semester:** 4th
