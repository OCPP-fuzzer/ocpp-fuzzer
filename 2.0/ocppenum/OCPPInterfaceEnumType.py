from enum import Enum
    
class OCPPInterfaceEnumType(Enum):
    WIRED0 = "Wired0" 
    WIRED1 = "Wired1" 
    WIRED2 = "Wired2" 
    WIRED3 = "Wired3" 
    WIRELESS0 = "Wireless0" 
    WIRELESS1 = "Wireless1" 
    WIRELESS2 = "Wireless2" 
    WIRELESS3 = "Wireless3" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    