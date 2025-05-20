from enum import Enum
    
class DataTransferStatusEnumType(Enum):
    ACCEPTED = "Accepted" 
    REJECTED = "Rejected" 
    UNKNOWN_MESSAGE_ID = "UnknownMessageId" 
    UNKNOWN_VENDOR_ID = "UnknownVendorId" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    