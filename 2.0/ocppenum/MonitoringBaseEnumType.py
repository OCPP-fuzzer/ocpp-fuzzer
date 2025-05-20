from enum import Enum
    
class MonitoringBaseEnumType(Enum):
    ALL = "All" 
    FACTORY_DEFAULT = "FactoryDefault" 
    HARD_WIRED_ONLY = "HardWiredOnly" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    