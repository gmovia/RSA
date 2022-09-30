from socket import *
from RSA import RSA

class Receiver:

    def __init__(self):
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        self.serverSocket.bind(('', 15011))

    def receive(self):
        self.serverSocket.listen(1)
        print("Escuchando..")
        connectionSocket, addr = self.serverSocket.accept()
        self.RSA = RSA(connectionSocket)
        while True:
            message = connectionSocket.recv(1024).decode()
            if message == "INIT": 
                connectionSocket.send(self.RSA.decrypt(message).encode())
            if message != "INIT":
                print("El mensaje descifrado que me llego es: ", self.RSA.decrypt(message))
                connectionSocket.close()
                break

receiver = Receiver()
receiver.receive()