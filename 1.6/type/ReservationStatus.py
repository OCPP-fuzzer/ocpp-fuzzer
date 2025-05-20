from enum import Enum
    
class ReservationStatus(Enum):

    """
    EnumType class
    : Accepted : Reservation has been made.
    : Faulted : Reservation has not been made, because connectors or specified connector are in a faulted state.
    : Occupied : Reservation has not been made. All connectors or the specified connector are occupied.
    : Rejected : Reservation has not been made. Charge Point is not configured to accept reservations.
    : Unavailable : Reservation has not been made, because connectors or specified connector are in an unavailable state.
    """

    ACCEPTED = "Accepted"
    FAULTED = "Faulted"
    OCCUPIED = "Occupied"
    REJECTED = "Rejected"
    UNAVAILABLE = "Unavailable"

    def get_value(self):
        return self.value

    @classmethod
    def get_members(cls):
        return [m for m in cls]

    @classmethod
    def get_sample(cls, option=False):
        value = __import__('random').choice(list(cls))
        return value.value
    