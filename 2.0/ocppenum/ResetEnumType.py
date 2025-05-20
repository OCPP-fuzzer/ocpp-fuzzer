from enum import Enum
    
class ResetEnumType(Enum):
    IMMEDIATE = "Immediate" 
    ON_IDLE = "OnIdle" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    