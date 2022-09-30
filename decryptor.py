class Decryptor:

    def decrypt(self, encryptedMessage, n, d):
        return pow(encryptedMessage, d, n)

