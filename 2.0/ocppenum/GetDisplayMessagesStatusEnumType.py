from enum import Enum
    
class GetDisplayMessagesStatusEnumType(Enum):
    ACCEPTED = "Accepted" 
    UNKNOWN = "Unknown" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    