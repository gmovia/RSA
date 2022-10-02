from socket import *
from RSA import RSA
from encoder import Encoder

class Sender:

    def __init__(self):
        self.RSA = RSA()
        self.clientSocket = socket(AF_INET, SOCK_STREAM)
        self.clientSocket.connect(('127.0.0.1', 12000))
        self.RSA.receivePublicKeys(self.clientSocket)
    
    def send(self, message):
        encryptedMessage = self.RSA.encrypt(message)
        self.clientSocket.send(Encoder.createDataSegment(encryptedMessage))
        self.clientSocket.close()

sender = Sender()
sender.send(19)
