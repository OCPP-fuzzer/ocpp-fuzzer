from enum import Enum
    
class ComponentCriterionEnumType(Enum):
    ACTIVE = "Active" 
    AVAILABLE = "Available" 
    ENABLED = "Enabled" 
    PROBLEM = "Problem" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    