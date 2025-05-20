from enum import Enum
    
class ChargingStateEnumType(Enum):
    CHARGING = "Charging" 
    E_V_CONNECTED = "EVConnected" 
    SUSPENDED_E_V = "SuspendedEV" 
    SUSPENDED_E_V_S_E = "SuspendedEVSE" 
    IDLE = "Idle" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    