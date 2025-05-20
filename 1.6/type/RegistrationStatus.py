from enum import Enum
    
class RegistrationStatus(Enum):

    """
    EnumType class
    : Accepted : Charge point is accepted by Central System.
    : Pending : Central System is not yet ready to accept the Charge Point. Central System may send messages to retrieve information or prepare the Charge Point.
    : Rejected : Charge point is not accepted by Central System. This may happen when the Charge Point id is not known by Central System.
    """

    ACCEPTED = "Accepted"
    PENDING = "Pending"
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
    