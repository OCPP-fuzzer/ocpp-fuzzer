from enum import Enum
    
class UpdateType(Enum):

    """
    EnumType class
    : Differential : Indicates that the current Local Authorization List must be updated with the values in this message.
    : Full : Indicates that the current Local Authorization List must be replaced by the values in this message.
    """

    DIFFERENTIAL = "Differential"
    FULL = "Full"

    def get_value(self):
        return self.value

    @classmethod
    def get_members(cls):
        return [m for m in cls]

    @classmethod
    def get_sample(cls, option=False):
        value = __import__('random').choice(list(cls))
        return value.value
    