from enum import Enum
    
class AuthorizationStatus(Enum):

    """
    EnumType class
    : Accepted : Identifier is allowed for charging.
    : Blocked : Identifier has been blocked. Not allowed for charging.
    : Expired : Identifier has expired. Not allowed for charging.
    : Invalid : Identifier is unknown. Not allowed for charging.
    : ConcurrentTx : Identifier is already involved in another transaction and multiple transactions are not allowed. (Only relevant for a StartTransaction.req.)
    """

    ACCEPTED = "Accepted"
    BLOCKED = "Blocked"
    EXPIRED = "Expired"
    INVALID = "Invalid"
    CONCURRENTTX = "ConcurrentTx"

    def get_value(self):
        return self.value

    @classmethod
    def get_members(cls):
        return [m for m in cls]

    @classmethod
    def get_sample(cls, option=False):
        value = __import__('random').choice(list(cls))
        return value.value
    