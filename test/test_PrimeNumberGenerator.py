import unittest
from src.primeNumberGenerator import PrimeNumberGenerator

class TestsPrimeNumberGenerator(unittest.TestCase):

    def test_7isAPrimeNumber(self):
        generator = PrimeNumberGenerator()
        self.assertTrue(generator.isPrime(7))
    
    def test02_12isNotAPrimeNumber(self):
        generator = PrimeNumberGenerator()
        self.assertFalse(generator.isPrime(12))

    def test03_RandomNumberIsAPrimeNumber(self):
        generator = PrimeNumberGenerator()
        for i in range(100):
            randomNumber = generator.generate()
            self.assertTrue(generator.isPrime(randomNumber))