from keyGenerator import KeyGenerator
from encoder import Encoder
from decoder import Decoder

class RSA:

    def __init__(self):
        self.generator = KeyGenerator()
        self.n, self.e, self.d = self.generator.generateKeys()
        self.n_received = 0
        self.e_received = 0

    def receivePublicKeys(self, socket):
        socket.send(Encoder.createInitiationSegment())
        segment = socket.recv(1024)
        self.n_received, self.e_received = Decoder.processPublicKeysSegment(segment)

    def sendPublicKeys(self, socket):
        socket.send(Encoder.createPublicKeysSegment(self.n, self.e))

    def encrypt(self, message):
        return pow(message, self.e_received, self.n_received)

    def decrypt(self, encryptedMessage):
        return pow(encryptedMessage, self.d, self.n)
