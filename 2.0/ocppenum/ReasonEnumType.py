from enum import Enum
    
class ReasonEnumType(Enum):
    DE_AUTHORIZED = "DeAuthorized" 
    EMERGENCY_STOP = "EmergencyStop" 
    ENERGY_LIMIT_REACHED = "EnergyLimitReached" 
    E_V_DISCONNECTED = "EVDisconnected" 
    GROUND_FAULT = "GroundFault" 
    IMMEDIATE_RESET = "ImmediateReset" 
    LOCAL = "Local" 
    LOCAL_OUT_OF_CREDIT = "LocalOutOfCredit" 
    MASTER_PASS = "MasterPass" 
    OTHER = "Other" 
    OVERCURRENT_FAULT = "OvercurrentFault" 
    POWER_LOSS = "PowerLoss" 
    POWER_QUALITY = "PowerQuality" 
    REBOOT = "Reboot" 
    REMOTE = "Remote" 
    S_O_C_LIMIT_REACHED = "SOCLimitReached" 
    STOPPED_BY_E_V = "StoppedByEV" 
    TIME_LIMIT_REACHED = "TimeLimitReached" 
    TIMEOUT = "Timeout" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    