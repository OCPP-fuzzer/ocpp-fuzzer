from enum import Enum
    
class Phase(Enum):

    """
    EnumType class
    : L1 : Measured on L1
    : L2 : Measured on L2
    : L3 : Measured on L3
    : N : Measured on Neutral
    """

    L1 = "L1"
    L2 = "L2"
    L3 = "L3"
    N = "N"

    def get_value(self):
        return self.value

    @classmethod
    def get_members(cls):
        return [m for m in cls]

    @classmethod
    def get_sample(cls, option=False):
        value = __import__('random').choice(list(cls))
        return value.value
    