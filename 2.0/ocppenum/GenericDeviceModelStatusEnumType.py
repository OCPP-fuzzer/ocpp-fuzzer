from enum import Enum
    
class GenericDeviceModelStatusEnumType(Enum):
    ACCEPTED = "Accepted" 
    REJECTED = "Rejected" 
    NOT_SUPPORTED = "NotSupported" 
    EMPTY_RESULT_SET = "EmptyResultSet" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    