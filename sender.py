from socket import *
from RSA import RSA

class Sender:

    def __init__(self):
        self.clientSocket = socket(AF_INET, SOCK_STREAM)
        self.clientSocket.connect(('127.0.0.1', 15011))
        self.RSA = RSA(self.clientSocket)
    
    def send(self, message):
        encryptedMessage = self.RSA.encrypt(message)
        self.clientSocket.send(str(encryptedMessage).encode())
        self.clientSocket.close()

sender = Sender()
sender.send(12345678)
