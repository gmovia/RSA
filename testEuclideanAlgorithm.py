import unittest
from euclideanAlgorithm import EuclideanAlgorithm

class TestEuclideanAlgorithm(unittest.TestCase):

    def test01_8Mcd8and24Is8(self):
        euclidean = EuclideanAlgorithm()
        self.assertEquals(euclidean.mcd(8, 24), 8)

    def test02_8Mcd123and45Is3(self):
        euclidean = EuclideanAlgorithm()
        self.assertEquals(euclidean.mcd(123, 45), 3)

    def test03_9123Mcd43and357Is1(self):
        euclidean = EuclideanAlgorithm()
        self.assertEquals(euclidean.mcd(9123, 43), 1)
    
    def test04_theReverse9inModule4Is1(self):
        euclidean = EuclideanAlgorithm()
        self.assertEquals(euclidean.reverse(9, 4), 1)

    def test05_theReverse28912inModule873Is178(self):
        euclidean = EuclideanAlgorithm()
        self.assertEquals(euclidean.reverse(28912, 873), 178)

    def test06_theReverse871inModule29Is1(self):
        euclidean = EuclideanAlgorithm()
        self.assertEquals(euclidean.reverse(871, 29), 1)
    
    def test07_theReverse1102inModule8IsFalse(self):
        euclidean = EuclideanAlgorithm()
        self.assertEquals(euclidean.reverse(11012, 8), False)

    def test08_theReverse2915inModule9Is8(self):
        euclidean = EuclideanAlgorithm()
        self.assertEquals(euclidean.reverse(2915, 9), 8)

if __name__ == '__main__':
    unittest.main()