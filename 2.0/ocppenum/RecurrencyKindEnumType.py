from enum import Enum
    
class RecurrencyKindEnumType(Enum):
    DAILY = "Daily" 
    WEEKLY = "Weekly" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    