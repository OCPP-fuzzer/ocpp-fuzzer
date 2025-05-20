from enum import Enum
    
class ChargingProfileKindEnumType(Enum):
    ABSOLUTE = "Absolute" 
    RECURRING = "Recurring" 
    RELATIVE = "Relative" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    