from enum import Enum
    
class DataTransferStatus(Enum):

    """
    EnumType class
    : Accepted : Message has been accepted and the contained request is accepted.
    : Rejected : Message has been accepted but the contained request is rejected.
    : UnknownMessageId : Message could not be interpreted due to unknown messageId string.
    : UnknownVendorId : Message could not be interpreted due to unknown vendorId string.
    """

    ACCEPTED = "Accepted"
    REJECTED = "Rejected"
    UNKNOWNMESSAGEID = "UnknownMessageId"
    UNKNOWNVENDORID = "UnknownVendorId"

    def get_value(self):
        return self.value

    @classmethod
    def get_members(cls):
        return [m for m in cls]

    @classmethod
    def get_sample(cls, option=False):
        value = __import__('random').choice(list(cls))
        return value.value
    