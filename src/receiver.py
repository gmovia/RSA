from socket import *
from RSA import RSA
from decoder import Decoder

class Receiver:

    def __init__(self):
        self.RSA = RSA()
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        self.serverSocket.bind(('', 12000))

    def receive(self):
        self.serverSocket.listen(1)
        connectionSocket, addr = self.serverSocket.accept()
        while True:
            segment = connectionSocket.recv(1024)
            if(Decoder.isInitiationSegment(segment)):
                self.RSA.sendPublicKeys(connectionSocket)
            else:
                 encryptedMessage = Decoder.processDataSegment(segment)
                 decryptedMessage = self.RSA.decrypt(encryptedMessage)
                 print(decryptedMessage)
                 break
    

receiver = Receiver()
receiver.receive()