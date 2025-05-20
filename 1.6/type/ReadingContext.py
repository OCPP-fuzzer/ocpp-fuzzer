from enum import Enum
    
class ReadingContext(Enum):

    """
    EnumType class
    : Other : Value for any other situations.
    : Trigger : Value taken in response to a TriggerMessage.req
    """

    OTHER = "Other"
    TRIGGER = "Trigger"

    def get_value(self):
        return self.value

    @classmethod
    def get_members(cls):
        return [m for m in cls]

    @classmethod
    def get_sample(cls, option=False):
        value = __import__('random').choice(list(cls))
        return value.value
    