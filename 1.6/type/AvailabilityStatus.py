from enum import Enum
    
class AvailabilityStatus(Enum):

    """
    EnumType class
    : Accepted : Request has been accepted and will be executed.
    : Rejected : Request has not been accepted and will not be executed.
    : Scheduled : Request has been accepted and will be executed when transaction(s) in progress have finished.
    """

    ACCEPTED = "Accepted"
    REJECTED = "Rejected"
    SCHEDULED = "Scheduled"

    def get_value(self):
        return self.value

    @classmethod
    def get_members(cls):
        return [m for m in cls]

    @classmethod
    def get_sample(cls, option=False):
        value = __import__('random').choice(list(cls))
        return value.value
    