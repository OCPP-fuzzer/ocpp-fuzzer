from enum import Enum
    
class RecurrencyKindType(Enum):

    """
    EnumType class
    : Daily : The schedule restarts every 24 hours, at the same time as in the startSchedule.
    : Weekly : The schedule restarts every 7 days, at the same time and day-of-the-week as in the startSchedule.
    """

    DAILY = "Daily"
    WEEKLY = "Weekly"

    def get_value(self):
        return self.value

    @classmethod
    def get_members(cls):
        return [m for m in cls]

    @classmethod
    def get_sample(cls, option=False):
        value = __import__('random').choice(list(cls))
        return value.value
    