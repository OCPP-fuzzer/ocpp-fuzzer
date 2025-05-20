from enum import Enum
    
class PhaseEnumType(Enum):
    L1 = "L1" 
    L2 = "L2" 
    L3 = "L3" 
    N = "N" 
    ## L1-N = "L1-N" 
    ## L2-N = "L2-N" 
    ## L3-N = "L3-N" 
    ## L1-L2 = "L1-L2" 
    ## L2-L3 = "L2-L3" 
    ## L3-L1 = "L3-L1" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    