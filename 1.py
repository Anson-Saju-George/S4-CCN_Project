from twisted.internet import protocol, reactor
from datetime import datetime

class HoneyPot(protocol.Protocol):
    def __init__(self):
        self.connections = 0

    def connectionMade(self):
        peer = self.transport.getPeer()
        self.connections += 1
        print(f"Connection from {peer.host}:{peer.port} at {datetime.now()}. Total connections: {self.connections}")

class HoneyPotFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return HoneyPot()

if __name__ == "__main__":
    port = 12345  # Change this to your desired port
    reactor.listenTCP(port, HoneyPotFactory())
    print(f"Honeypot listening on port {port}...")
    reactor.run()
