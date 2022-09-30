from encryptor import Encryptor
from decryptor import Decryptor
from keyGenerator import KeyGenerator

class RSA:

    def __init__(self, clientSocket):
        self.generator = KeyGenerator()
        self.publicKeys, self.privateKeys = self.generator.generateKeys()
        self.encryptor = Encryptor()
        self.decryptor = Decryptor()
        self.clientSocket = clientSocket

    def encrypt(self, message):
        self.clientSocket.send("INIT".encode())
        receiversPublicKeys = self.clientSocket.recv(1024).decode().split()
        return self.encryptor.encrypt(message, int(receiversPublicKeys[0]), int(receiversPublicKeys[1])) # (n, e)

    def decrypt(self, encryptedMessage):
        if(encryptedMessage == "INIT"):
            return str(self.publicKeys[0])+" "+str(self.publicKeys[1])
        return self.decryptor.decrypt(int(encryptedMessage), self.privateKeys[0], self.privateKeys[1]) # (n, d)
