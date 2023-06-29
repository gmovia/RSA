class Encoder:

    @classmethod
    def createInitiationSegment(self):
        return "0".encode()
        
    @classmethod
    def createPublicKeysSegment(self, n, e):
        return ("1" + " " + str(n) + " " + str(e)).encode()

    @classmethod
    def createDataSegment(self, message):
        return ("2" + " " + str(message)).encode()
