from enum import Enum
    
class ChargingProfileKindType(Enum):

    """
    EnumType class
    : Absolute : Schedule periods are relative to a fixed point in time defined in the schedule.
    : Recurring : The schedule restarts periodically at the first schedule period.
    : Relative : Schedule periods are relative to a situation-specific start point (such as the start of a Transaction) that is determined by the charge point.
    """

    ABSOLUTE = "Absolute"
    RECURRING = "Recurring"
    RELATIVE = "Relative"

    def get_value(self):
        return self.value

    @classmethod
    def get_members(cls):
        return [m for m in cls]

    @classmethod
    def get_sample(cls, option=False):
        value = __import__('random').choice(list(cls))
        return value.value
    