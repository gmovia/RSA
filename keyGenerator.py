from primeNumberGenerator import PrimeNumberGenerator
from euclideanAlgorithm import EuclideanAlgorithm

class KeyGenerator:

    def __init__(self):
        self.generator = PrimeNumberGenerator()
        self.euclidean = EuclideanAlgorithm()
        self.p = self.generator.generate()
        self.q = self.generator.generate()
        self.n = self.p*self.q
        self.phi_n = (self.p-1)*(self.q-1)

    def generatePublicKeys(self):
        for i in range(2, self.phi_n):
            if(self.euclidean.mcd(i, self.phi_n) == 1):
                return (self.n, i)

    def generatePrivateKeys(self, e):
        return (self.n, self.euclidean.reverse(e, self.phi_n))

    def generateKeys(self):
        publicKeys = self.generatePublicKeys()
        privateKeys = self.generatePrivateKeys(publicKeys[1])
        return (publicKeys, privateKeys)

