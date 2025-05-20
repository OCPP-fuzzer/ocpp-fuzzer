from enum import Enum
    
class HashAlgorithmEnumType(Enum):
    SHA256 = "SHA256" 
    SHA384 = "SHA384" 
    SHA512 = "SHA512" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    