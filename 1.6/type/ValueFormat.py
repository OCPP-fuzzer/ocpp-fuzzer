from enum import Enum
    
class ValueFormat(Enum):

    """
    EnumType class
    : Raw : Data is to be interpreted as integer/decimal numeric data.
    : SignedData : Data is represented as a signed binary data block, encoded as hex data.
    """

    RAW = "Raw"
    SIGNEDDATA = "SignedData"

    def get_value(self):
        return self.value

    @classmethod
    def get_members(cls):
        return [m for m in cls]

    @classmethod
    def get_sample(cls, option=False):
        value = __import__('random').choice(list(cls))
        return value.value
    