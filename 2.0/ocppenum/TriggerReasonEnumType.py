from enum import Enum
    
class TriggerReasonEnumType(Enum):
    AUTHORIZED = "Authorized" 
    CABLE_PLUGGED_IN = "CablePluggedIn" 
    CHARGING_RATE_CHANGED = "ChargingRateChanged" 
    CHARGING_STATE_CHANGED = "ChargingStateChanged" 
    DEAUTHORIZED = "Deauthorized" 
    ENERGY_LIMIT_REACHED = "EnergyLimitReached" 
    E_V_COMMUNICATION_LOST = "EVCommunicationLost" 
    E_V_CONNECT_TIMEOUT = "EVConnectTimeout" 
    METER_VALUE_CLOCK = "MeterValueClock" 
    METER_VALUE_PERIODIC = "MeterValuePeriodic" 
    TIME_LIMIT_REACHED = "TimeLimitReached" 
    TRIGGER = "Trigger" 
    UNLOCK_COMMAND = "UnlockCommand" 
    STOP_AUTHORIZED = "StopAuthorized" 
    E_V_DEPARTED = "EVDeparted" 
    E_V_DETECTED = "EVDetected" 
    REMOTE_STOP = "RemoteStop" 
    REMOTE_START = "RemoteStart" 
    ABNORMAL_CONDITION = "AbnormalCondition" 
    SIGNED_DATA_RECEIVED = "SignedDataReceived" 
    RESET_COMMAND = "ResetCommand" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    