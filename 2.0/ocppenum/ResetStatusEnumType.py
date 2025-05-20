from enum import Enum
    
class ResetStatusEnumType(Enum):
    ACCEPTED = "Accepted" 
    REJECTED = "Rejected" 
    SCHEDULED = "Scheduled" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    