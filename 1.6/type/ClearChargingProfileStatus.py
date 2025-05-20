from enum import Enum
    
class ClearChargingProfileStatus(Enum):

    """
    EnumType class
    : Accepted : Request has been accepted and will be executed.
    : Unknown : No Charging Profile(s) were found matching the request.
    """

    ACCEPTED = "Accepted"
    UNKNOWN = "Unknown"

    def get_value(self):
        return self.value

    @classmethod
    def get_members(cls):
        return [m for m in cls]

    @classmethod
    def get_sample(cls, option=False):
        value = __import__('random').choice(list(cls))
        return value.value
    