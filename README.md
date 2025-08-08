# Secure Blockchain Communication Network (CCN Project)

## 🎯 Project Overview
This repository contains a comprehensive **Computer Communication Networks (CCN)** project developed during my **Fourth Semester**. The project demonstrates advanced network security, blockchain integration, and secure communication protocols using Python, implementing RSA encryption, Ethereum smart contracts, ARP spoofing detection, and honeypot security systems.

## 📋 Project Details
- **Student:** Anson Saju George
- **Semester:** 4th Semester
- **Course:** Computer Communication Networks (CCN)
- **Focus Areas:** Network Security, Blockchain Technology, Cryptography
- **Technology Stack:** Python, Web3.py, Ethereum, Solidity, RSA Encryption
- **Development Environment:** Ganache, Truffle Framework

## 🔧 System Architecture

### Core Components
1. **RSA Encryption System** - Secure client-server communication
2. **Ethereum Blockchain Integration** - Smart contract deployment and interaction
3. **Network Security Tools** - ARP spoofing detection and honeypot systems
4. **Multi-Client Communication** - Encrypted peer-to-peer messaging
5. **Balance Management** - Ethereum wallet balance checking

## 📁 Repository Structure
```
├── README.md                           # Project documentation
├── Server.py                          # Secure server with RSA decryption
├── ClientA.py                         # Client A with RSA encryption
├── ClientB.py                         # Client B with RSA encryption
├── Both.py                            # Dual client implementation
├── RSA.py                             # RSA key generation utility
├── RSA2.py                            # Enhanced RSA communication
├── Solidity.py                        # Smart contract deployment
├── Balance.py                         # Ethereum balance checker
├── Test_Run.py                        # AES encryption testing
├── run.py                             # Solidity compiler setup
├── 1.py                               # Honeypot security system
├── truffle.js                         # Truffle configuration
├── Spoof/                             # Network security tools
│   └── A.py                          # ARP spoofing detection
├── Certificates/                      # RSA key pairs
│   ├── client_a_private.pem          # Client A private key
│   ├── client_a_public.pem           # Client A public key
│   ├── client_b_private.pem          # Client B private key
│   └── client_b_public.pem           # Client B public key
└── tempCodeRunnerFile.py             # Development testing
```

## 🔐 Security Implementation

### RSA Encryption System
- **Key Size:** 2048-bit RSA keys for robust security
- **Encryption Standard:** PKCS1_OAEP padding scheme
- **Key Management:** Separate key pairs for each client
- **Secure Communication:** End-to-end encrypted messaging

#### Key Generation
```python
def generate_rsa_key_pair(filename):
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
```

#### Encryption/Decryption Process
```python
def encrypt_message(message, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    return cipher.encrypt(message.encode())

def decrypt_message(encrypted_message, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    return cipher.decrypt(encrypted_message)
```

### AES Encryption Integration
- **Symmetric Encryption:** AES with CBC mode
- **Random Key Generation:** 128-bit AES keys
- **Padding:** PKCS7 padding for block alignment
- **Digital Signatures:** SHA-256 hash-based message authentication

## ⛓️ Blockchain Integration

### Ethereum Smart Contracts
```solidity
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
```

### Web3.py Integration
- **Local Blockchain:** Ganache development environment
- **Smart Contract Compilation:** Solidity compiler integration
- **Contract Deployment:** Automated deployment scripts
- **Balance Management:** Real-time Ethereum balance checking

### Network Configuration
```javascript
networks: {
    development: {
        host: "127.0.0.1",
        port: 7545,
        network_id: "*",
    },
    rinkeby: {
        host: "localhost", 
        port: 7545,
        network_id: 4,
        gas: 6000000,
    }
}
```

## 🛡️ Network Security Features

### ARP Spoofing Detection
```python
def process_packet(packet):
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
        real_mac = get_mac(packet[scapy.ARP].psrc)
        response_mac = packet[scapy.ARP].hwsrc
        if real_mac != response_mac:
            print("[!] Possible ARP Spoofing Attack Detected!")
```

### Honeypot Security System
- **Connection Monitoring:** Real-time intrusion detection
- **Logging:** Timestamp and IP tracking
- **Port Scanning Detection:** Unauthorized access attempts
- **Network Forensics:** Connection pattern analysis

## 💻 Communication Architecture

### Multi-Client Server Model
- **Server Configuration:** TCP socket server on port 12345
- **Client Authentication:** RSA key-based client identification
- **Encrypted Messaging:** All communications RSA encrypted
- **Real-time Communication:** Bidirectional message exchange

### Communication Flow
1. **Key Exchange:** Clients exchange public keys
2. **Connection Establishment:** TCP socket connections
3. **Message Encryption:** RSA encryption before transmission
4. **Secure Transmission:** Encrypted data over network
5. **Decryption:** Server/client decryption using private keys

## 🚀 Getting Started

### Prerequisites
```bash
# Install required Python packages
pip install pycryptodome
pip install web3
pip install py-solc-x
pip install scapy
pip install twisted

# Install Ganache for local blockchain
# Download from: https://trufflesuite.com/ganache/
```

### Setup Instructions

#### 1. Blockchain Environment Setup
```bash
# Start Ganache local blockchain
# Configure RPC Server: http://127.0.0.1:7545
# Note the account addresses and private keys
```

#### 2. RSA Key Generation
```bash
python RSA.py  # Generate server/client key pairs
```

#### 3. Smart Contract Deployment
```bash
python run.py      # Install Solidity compiler
python Solidity.py # Deploy smart contracts
```

#### 4. Run Communication System
```bash
# Terminal 1: Start the server
python Server.py

# Terminal 2: Start Client A
python ClientA.py

# Terminal 3: Start Client B  
python ClientB.py
```

#### 5. Security Monitoring
```bash
# ARP spoofing detection
sudo python Spoof/A.py

# Honeypot monitoring
python 1.py
```

## 📊 System Capabilities

### Secure Communication Features
- **End-to-End Encryption:** RSA 2048-bit encryption
- **Key Management:** Automated key generation and distribution
- **Message Integrity:** Cryptographic hash verification
- **Session Security:** Unique session keys for each communication

### Blockchain Features
- **Smart Contract Integration:** Solidity contract deployment
- **Balance Management:** Real-time account balance checking
- **Transaction Processing:** Ethereum transaction handling
- **Decentralized Storage:** Blockchain-based data storage

### Security Monitoring
- **Network Intrusion Detection:** Real-time monitoring
- **ARP Attack Prevention:** Layer 2 security
- **Connection Logging:** Comprehensive audit trails
- **Traffic Analysis:** Network behavior monitoring

## 🎓 Learning Outcomes
This comprehensive CCN project provided hands-on experience with:
- **Network Security Protocols:** RSA, AES encryption implementation
- **Blockchain Technology:** Ethereum, smart contracts, Web3.py
- **Socket Programming:** TCP/UDP communication protocols
- **Cryptography:** Public-key and symmetric encryption
- **Network Monitoring:** Intrusion detection systems
- **System Security:** Honeypot deployment and monitoring
- **Distributed Systems:** Peer-to-peer communication architecture

## 🔬 Technical Innovations

### Multi-Layer Security Architecture
1. **Application Layer:** RSA encryption for message security
2. **Transport Layer:** TCP socket secure communication
3. **Network Layer:** ARP spoofing detection
4. **Physical Layer:** Network traffic monitoring

### Advanced Encryption Implementation
- **Hybrid Encryption:** RSA for key exchange, AES for data
- **Digital Signatures:** Message authentication and non-repudiation
- **Key Rotation:** Dynamic key generation capabilities
- **Forward Secrecy:** Session-based security protocols

## 📈 Future Enhancements
- **Mobile Application:** Android/iOS client applications
- **Web Interface:** Browser-based communication platform
- **Advanced Cryptography:** Elliptic Curve Cryptography (ECC)
- **Blockchain Optimization:** Layer 2 scaling solutions
- **Machine Learning:** AI-based intrusion detection
- **IoT Integration:** Internet of Things device communication

## 🛠️ Hardware Requirements
- **Minimum RAM:** 4GB (8GB recommended)
- **Storage:** 10GB available space
- **Network:** Ethernet/Wi-Fi connectivity
- **Operating System:** Linux/Windows/macOS
- **Python Version:** 3.8 or higher

## 📚 Technical Documentation

### API Endpoints
- **Server:** `127.0.0.1:12345` (RSA encrypted communication)
- **Blockchain:** `127.0.0.1:7545` (Ganache local node)
- **Honeypot:** `127.0.0.1:12345` (Security monitoring)

### Configuration Files
- **truffle.js:** Blockchain network configuration
- **RSA Keys:** Client/server cryptographic certificates
- **Solidity Contracts:** Smart contract source code

## 🏆 Project Achievements
- **Complete Security Suite:** Multi-layered network security
- **Blockchain Integration:** Full Ethereum ecosystem implementation
- **Real-time Communication:** Secure messaging platform
- **Network Monitoring:** Comprehensive security analysis
- **Cryptographic Implementation:** Industry-standard encryption

## 📖 Academic Context
This project demonstrates advanced concepts in:
- **Computer Networks:** TCP/IP, socket programming, network protocols
- **Cryptography:** RSA, AES, digital signatures, key management
- **Blockchain Technology:** Smart contracts, decentralized applications
- **System Security:** Intrusion detection, network forensics
- **Software Engineering:** Multi-module architecture, API design

---
**Note:** This is an academic project showcasing advanced network security, blockchain integration, and secure communication protocols for educational purposes in Computer Communication Networks coursework.