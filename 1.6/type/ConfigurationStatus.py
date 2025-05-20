from enum import Enum
    
class ConfigurationStatus(Enum):

    """
    EnumType class
    : Accepted : Configuration key is supported and setting has been changed.
    : Rejected : Configuration key is supported, but setting could not be changed.
    : RebootRequired : Configuration key is supported and setting has been changed, but change will be available after reboot (Charge Point will not reboot itself)
    : NotSupported : Configuration key is not supported.
    """

    ACCEPTED = "Accepted"
    REJECTED = "Rejected"
    REBOOTREQUIRED = "RebootRequired"
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
    