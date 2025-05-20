from enum import Enum
    
class MonitoringCriterionEnumType(Enum):
    THRESHOLD_MONITORING = "ThresholdMonitoring" 
    DELTA_MONITORING = "DeltaMonitoring" 
    PERIODIC_MONITORING = "PeriodicMonitoring" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    