from enum import Enum
    
class UnlockStatus(Enum):

    """
    EnumType class
    : Unlocked : Connector has successfully been unlocked.
    : UnlockFailed : Failed to unlock the connector: The Charge Point has tried to unlock the connector and has detected that the connector is still locked or the unlock mechanism failed.
    : NotSupported : Charge Point has no connector lock, or ConnectorId is unknown.
    """

    UNLOCKED = "Unlocked"
    UNLOCKFAILED = "UnlockFailed"
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
    