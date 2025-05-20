from enum import Enum
    
class NotifyEVChargingNeedsStatusEnumType(Enum):
    ACCEPTED = "Accepted" 
    REJECTED = "Rejected" 
    PROCESSING = "Processing" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    