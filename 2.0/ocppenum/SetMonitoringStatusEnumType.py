from enum import Enum
    
class SetMonitoringStatusEnumType(Enum):
    ACCEPTED = "Accepted" 
    UNKNOWN_COMPONENT = "UnknownComponent" 
    UNKNOWN_VARIABLE = "UnknownVariable" 
    UNSUPPORTED_MONITOR_TYPE = "UnsupportedMonitorType" 
    REJECTED = "Rejected" 
    DUPLICATE = "Duplicate" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    