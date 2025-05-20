from enum import Enum
    
class DeleteCertificateStatusEnumType(Enum):
    ACCEPTED = "Accepted" 
    FAILED = "Failed" 
    NOT_FOUND = "NotFound" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    