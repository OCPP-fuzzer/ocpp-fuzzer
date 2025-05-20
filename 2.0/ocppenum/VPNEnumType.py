from enum import Enum
    
class VPNEnumType(Enum):
    I_K_EV2 = "IKEv2" 
    I_P_SEC = "IPSec" 
    L2TP = "L2TP" 
    PPTP = "PPTP" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    