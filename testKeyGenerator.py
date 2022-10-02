import unittest
from keyGenerator import KeyGenerator
from euclideanAlgorithm import EuclideanAlgorithm

class TestKeyGenerator(unittest.TestCase):

    def test01_PhiNIsCoprimeOfE(self):
        generator = KeyGenerator()
        euclidean = EuclideanAlgorithm()
        n, e = generator.generatePublicKeys()
        self.assertEquals(euclidean.mcd(e, generator.phi_n), 1)

    def test02_TheInverseMultiplicativeOfEinPhiNIsD(self):
        generator = KeyGenerator()
        euclidean = EuclideanAlgorithm()
        n, e, d = generator.generateKeys()
        self.assertEquals(euclidean.reverse(e, generator.phi_n), d)

if __name__ == '__main__':
    unittest.main()