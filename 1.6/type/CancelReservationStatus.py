from enum import Enum
    
class CancelReservationStatus(Enum):

    """
    EnumType class
    : Accepted : Reservation for the identifier has been cancelled.
    : Rejected : Reservation could not be cancelled, because there is no reservation active for the identifier.
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
    