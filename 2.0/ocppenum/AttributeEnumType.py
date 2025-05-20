from enum import Enum
    
class AttributeEnumType(Enum):
    ACTUAL = "Actual" 
    TARGET = "Target" 
    MIN_SET = "MinSet" 
    MAX_SET = "MaxSet" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    