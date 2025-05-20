from enum import Enum
    
class EventTriggerEnumType(Enum):
    ALERTING = "Alerting" 
    DELTA = "Delta" 
    PERIODIC = "Periodic" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    