from ocppenum.HashAlgorithmEnumType import HashAlgorithmEnumType

identifierString = str

class OCSPRequestDataType:
    def __init__(self, hashAlgorithm: HashAlgorithmEnumType, issuerNameHash: identifierString, issuerKeyHash: str, serialNumber: identifierString, responderURL: str):
        self.hashAlgorithm = hashAlgorithm
        self.issuerNameHash = issuerNameHash
        self.issuerKeyHash = issuerKeyHash
        self.serialNumber = serialNumber
        self.responderURL = responderURL

    def to_dict(self):
        request = {
            "hashAlgorithm" : self.hashAlgorithm.value,
            "issuerNameHash" : self.issuerNameHash,
            "issuerKeyHash" : self.issuerKeyHash,
            "serialNumber" : self.serialNumber,
            "responderURL" : self.responderURL,
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['hashAlgorithm'] = HashAlgorithmEnumType.sample()
        result['issuerNameHash'] = str(__import__('uuid').uuid4())
        result['issuerKeyHash'] = "string"
        result['serialNumber'] = str(__import__('uuid').uuid4())
        result['responderURL'] = "string"

        return result
    