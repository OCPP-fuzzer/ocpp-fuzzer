from enum import Enum
    
class LocationEnumType(Enum):
    BODY = "Body" 
    CABLE = "Cable" 
    EV = "EV" 
    INLET = "Inlet" 
    OUTLET = "Outlet" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    