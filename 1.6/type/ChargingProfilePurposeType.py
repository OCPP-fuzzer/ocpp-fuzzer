from enum import Enum
    
class ChargingProfilePurposeType(Enum):

    """
    EnumType class
    : ChargePointMaxProfile : Configuration for the maximum power or current available for an entire Charge Point.
    : TxDefaultProfile : Default profile *that can be configured in the Charge Point. When a new transaction is started, this profile SHALL be used, unless it was a transaction that was started by a RemoteStartTransaction.req with a ChargeProfile that is accepted by the Charge Point.
    : TxProfile : Profile with constraints to be imposed by the Charge Point on the current transaction, or on a new transaction when this is started via a RemoteStartTransaction.req with a ChargeProfile. A profile with this purpose SHALL cease to be valid when the transaction terminates.
    """

    CHARGEPOINTMAXPROFILE = "ChargePointMaxProfile"
    TXDEFAULTPROFILE = "TxDefaultProfile"
    TXPROFILE = "TxProfile"

    def get_value(self):
        return self.value

    @classmethod
    def get_members(cls):
        return [m for m in cls]

    @classmethod
    def get_sample(cls, option=False):
        value = __import__('random').choice(list(cls))
        return value.value
    