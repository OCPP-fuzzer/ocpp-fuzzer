from enum import Enum
    
class ReserveNowStatusEnumType(Enum):
    ACCEPTED = "Accepted" 
    FAULTED = "Faulted" 
    OCCUPIED = "Occupied" 
    REJECTED = "Rejected" 
    UNAVAILABLE = "Unavailable" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    