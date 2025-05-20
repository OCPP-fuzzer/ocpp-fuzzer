from enum import Enum
    
class ClearCacheStatus(Enum):

    """
    EnumType class
    : Accepted : Command has been executed.
    : Rejected : Command has not been executed.
    """

    ACCEPTED = "Accepted"
    REJECTED = "Rejected"

    def get_value(self):
        return self.value

    @classmethod
    def get_members(cls):
        return [m for m in cls]

    @classmethod
    def get_sample(cls, option=False):
        value = __import__('random').choice(list(cls))
        return value.value
    