from enum import Enum
    
class UpdateStatus(Enum):

    """
    EnumType class
    : Accepted : Local Authorization List successfully updated.
    : Failed : Failed to update the Local Authorization List.
    : NotSupported : Update of Local Authorization List is not supported by Charge Point.
    : VersionMismatch : Version number in the request for a differential update is less or equal then version number of current list.
    """

    ACCEPTED = "Accepted"
    FAILED = "Failed"
    NOTSUPPORTED = "NotSupported"
    VERSIONMISMATCH = "VersionMismatch"

    def get_value(self):
        return self.value

    @classmethod
    def get_members(cls):
        return [m for m in cls]

    @classmethod
    def get_sample(cls, option=False):
        value = __import__('random').choice(list(cls))
        return value.value
    