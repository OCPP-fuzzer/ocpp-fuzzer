identifierString = str

class UnpublishFirmwareRequest:
    def __init__(self, checksum: identifierString):
        self.checksum = checksum

    def to_dict(self):
        request = {
            "checksum" : self.checksum,
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['checksum'] = str(__import__('uuid').uuid4())

        return result
    