from enum import Enum
    
class ChargingProfileStatus(Enum):

    """
    EnumType class
    : Accepted : Request has been accepted and will be executed.
    : Rejected : Request has not been accepted and will not be executed.
    : NotSupported : Charge Point indicates that the request is not supported.
    """

    ACCEPTED = "Accepted"
    REJECTED = "Rejected"
    NOTSUPPORTED = "NotSupported"

    def get_value(self):
        return self.value

    @classmethod
    def get_members(cls):
        return [m for m in cls]

    @classmethod
    def get_sample(cls, option=False):
        value = __import__('random').choice(list(cls))
        return value.value
    