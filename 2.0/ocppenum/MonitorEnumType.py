from enum import Enum
    
class MonitorEnumType(Enum):
    UPPER_THRESHOLD = "UpperThreshold" 
    LOWER_THRESHOLD = "LowerThreshold" 
    DELTA = "Delta" 
    PERIODIC = "Periodic" 
    PERIODIC_CLOCK_ALIGNED = "PeriodicClockAligned" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    