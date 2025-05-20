from enum import Enum
    
class BootReasonEnumType(Enum):
    APPLICATION_RESET = "ApplicationReset" 
    FIRMWARE_UPDATE = "FirmwareUpdate" 
    LOCAL_RESET = "LocalReset" 
    POWER_UP = "PowerUp" 
    REMOTE_RESET = "RemoteReset" 
    SCHEDULED_RESET = "ScheduledReset" 
    TRIGGERED = "Triggered" 
    UNKNOWN = "Unknown" 
    WATCHDOG = "Watchdog" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    