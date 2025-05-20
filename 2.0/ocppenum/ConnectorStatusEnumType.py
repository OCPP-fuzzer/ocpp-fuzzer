from enum import Enum
    
class ConnectorStatusEnumType(Enum):
    AVAILABLE = "Available" 
    OCCUPIED = "Occupied" 
    RESERVED = "Reserved" 
    UNAVAILABLE = "Unavailable" 
    FAULTED = "Faulted" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    