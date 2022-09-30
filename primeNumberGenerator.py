import random

class PrimeNumberGenerator:

    def isPrime(self, number):
        for i in range(2, number):
            if number%i == 0:
                return False
        return True

    def generate(self):
        while True:
            number = random.randint(1, 10000)
            if self.isPrime(number) == True:
                return number

