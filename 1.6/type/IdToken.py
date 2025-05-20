from enum import Enum
    
class IdToken(Enum):

    """
    EnumType class
    : CiString20Type : IdToken is case insensitive.
    """

    CISTRING20TYPE = "CiString20Type"

    def get_value(self):
        return self.value

    @classmethod
    def get_members(cls):
        return [m for m in cls]

    @classmethod
    def get_sample(cls, option=False):
        value = __import__('random').choice(list(cls))
        return value.value
    