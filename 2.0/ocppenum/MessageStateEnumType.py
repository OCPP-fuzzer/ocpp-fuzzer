from enum import Enum
    
class MessageStateEnumType(Enum):
    CHARGING = "Charging" 
    FAULTED = "Faulted" 
    IDLE = "Idle" 
    UNAVAILABLE = "Unavailable" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    