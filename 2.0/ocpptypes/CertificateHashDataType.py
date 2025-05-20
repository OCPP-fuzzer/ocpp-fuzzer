from ocppenum.HashAlgorithmEnumType import HashAlgorithmEnumType

identifierString = str

class CertificateHashDataType:
    def __init__(self, hashAlgorithm: HashAlgorithmEnumType, issuerNameHash: identifierString, issuerKeyHash: str, serialNumber: identifierString):
        self.hashAlgorithm = hashAlgorithm
        self.issuerNameHash = issuerNameHash
        self.issuerKeyHash = issuerKeyHash
        self.serialNumber = serialNumber

    def to_dict(self):
        request = {
            "hashAlgorithm" : self.hashAlgorithm.value,
            "issuerNameHash" : self.issuerNameHash,
            "issuerKeyHash" : self.issuerKeyHash,
            "serialNumber" : self.serialNumber,
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['hashAlgorithm'] = HashAlgorithmEnumType.sample()
        result['issuerNameHash'] = str(__import__('uuid').uuid4())
        result['issuerKeyHash'] = "string"
        result['serialNumber'] = str(__import__('uuid').uuid4())

        return result
    