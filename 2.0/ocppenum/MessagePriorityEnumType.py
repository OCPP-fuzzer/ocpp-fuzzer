from enum import Enum
    
class MessagePriorityEnumType(Enum):
    ALWAYS_FRONT = "AlwaysFront" 
    IN_FRONT = "InFront" 
    NORMAL_CYCLE = "NormalCycle" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    