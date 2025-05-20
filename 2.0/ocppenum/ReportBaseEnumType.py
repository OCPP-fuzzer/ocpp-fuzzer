from enum import Enum
    
class ReportBaseEnumType(Enum):
    CONFIGURATION_INVENTORY = "ConfigurationInventory" 
    FULL_INVENTORY = "FullInventory" 
    SUMMARY_INVENTORY = "SummaryInventory" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    