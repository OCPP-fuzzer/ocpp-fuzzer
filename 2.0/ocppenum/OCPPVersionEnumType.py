from enum import Enum
    
class OCPPVersionEnumType(Enum):
    OCPP12 = "OCPP12" 
    OCPP15 = "OCPP15" 
    OCPP16 = "OCPP16" 
    OCPP20 = "OCPP20" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    