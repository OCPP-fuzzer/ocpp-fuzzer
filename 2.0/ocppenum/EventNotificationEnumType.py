from enum import Enum
    
class EventNotificationEnumType(Enum):
    HARD_WIRED_NOTIFICATION = "HardWiredNotification" 
    HARD_WIRED_MONITOR = "HardWiredMonitor" 
    PRECONFIGURED_MONITOR = "PreconfiguredMonitor" 
    CUSTOM_MONITOR = "CustomMonitor" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    