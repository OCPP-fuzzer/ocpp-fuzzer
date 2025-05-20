from enum import Enum
    
class MutabilityEnumType(Enum):
    READ_ONLY = "ReadOnly" 
    WRITE_ONLY = "WriteOnly" 
    READ_WRITE = "ReadWrite" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    