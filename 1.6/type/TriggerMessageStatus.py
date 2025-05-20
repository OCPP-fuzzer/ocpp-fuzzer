from enum import Enum
    
class TriggerMessageStatus(Enum):

    """
    EnumType class
    : Accepted : Requested notification will be sent.
    : Rejected : Requested notification will not be sent.
    : NotImplemented : Requested notification cannot be sent because it is either not implemented or unknown.
    """

    ACCEPTED = "Accepted"
    REJECTED = "Rejected"
    NOTIMPLEMENTED = "NotImplemented"

    def get_value(self):
        return self.value

    @classmethod
    def get_members(cls):
        return [m for m in cls]

    @classmethod
    def get_sample(cls, option=False):
        value = __import__('random').choice(list(cls))
        return value.value
    