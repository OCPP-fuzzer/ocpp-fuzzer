from enum import Enum
    
class DisplayMessageStatusEnumType(Enum):
    ACCEPTED = "Accepted" 
    NOT_SUPPORTED_MESSAGE_FORMAT = "NotSupportedMessageFormat" 
    REJECTED = "Rejected" 
    NOT_SUPPORTED_PRIORITY = "NotSupportedPriority" 
    NOT_SUPPORTED_STATE = "NotSupportedState" 
    UNKNOWN_TRANSACTION = "UnknownTransaction" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    