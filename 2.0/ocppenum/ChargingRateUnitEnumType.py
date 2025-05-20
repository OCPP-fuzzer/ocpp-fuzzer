from enum import Enum
    
class ChargingRateUnitEnumType(Enum):
    W = "W" 
    A = "A" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    