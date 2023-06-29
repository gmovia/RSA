import unittest
from src.RSA import RSA

class TestRSA(unittest.TestCase):

    # n = 3233 ; e = 17  ; d = 2753 ; M < n
    def test01_siElMensajeEs1234entoncesElCifradoEs2183(self):
        rsa = RSA()
        rsa.n_received = 3233 # n del receptor
        rsa.e_received = 17 # e del receptor
        self.assertEqual(rsa.encrypt(1234), 2183)

    def test02_siElMensajeCifradoEs2183entoncesElMensajeOriginalEs1234(self):
        rsa = RSA()
        rsa.n = 3233 
        rsa.d = 2753 
        self.assertEqual(rsa.decrypt(2183), 1234)

    # n = 1416383 ; e = 7 ; d = 1211863 ; m tiene que ser menor que n
    def test03_siElMensajeEs1234567entoncesElCifradoEs331502(self):
        rsa = RSA()
        rsa.n_received = 1416383 # n del receptor
        rsa.e_received = 7 # e del receptor
        self.assertEqual(rsa.encrypt(1234567), 331502)

    def test04_siElMensajeCifradoEs331502entoncesElMensajeOriginalEs1234567(self):
        rsa = RSA()
        rsa.n = 1416383 
        rsa.d = 1211863
        self.assertEqual(rsa.decrypt(331502), 1234567)