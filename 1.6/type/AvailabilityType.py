from enum import Enum
    
class AvailabilityType(Enum):

    """
    EnumType class
    : Inoperative : Charge point is not available for charging.
    : Operative : Charge point is available for charging.
    """

    INOPERATIVE = "Inoperative"
    OPERATIVE = "Operative"

    def get_value(self):
        return self.value

    @classmethod
    def get_members(cls):
        return [m for m in cls]

    @classmethod
    def get_sample(cls, option=False):
        value = __import__('random').choice(list(cls))
        return value.value
    