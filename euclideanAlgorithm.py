class EuclideanAlgorithm:

    def mcd(self, number, otherNumber):
        if otherNumber == 0:
            return number
        return self.mcd(otherNumber, number%otherNumber)

    def reverse(self, number, module):
        for x in range(1,module):
            if((number % module)*(x % module) % module == 1):
                return x

