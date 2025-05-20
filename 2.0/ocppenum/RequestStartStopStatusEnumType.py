from enum import Enum
    
class RequestStartStopStatusEnumType(Enum):
    ACCEPTED = "Accepted" 
    REJECTED = "Rejected" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    