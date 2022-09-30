class Encryptor:

    def encrypt(self, message, n, e):
        return pow(message, e, n)

