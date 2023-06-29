class Decoder:

    @classmethod
    def isInitiationSegment(self, segment):
        return segment.decode().split()[0] == "0"

    @classmethod
    def isPublicKeySegment(self, segment):
        return segment.decode().split()[0] == "1"

    @classmethod
    def isDataSegment(self, segment):
        return segment.decode().split()[0] == "2"

    @classmethod
    def processDataSegment(self, segment):
        array = segment.decode().split()
        return int(array[1]) # message
    
    @classmethod
    def processPublicKeysSegment(self, segment):
        array = segment.decode().split()
        return int(array[1]), int(array[2]) # n, e


