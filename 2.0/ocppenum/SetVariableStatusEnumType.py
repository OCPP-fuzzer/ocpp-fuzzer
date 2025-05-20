from enum import Enum
    
class SetVariableStatusEnumType(Enum):
    ACCEPTED = "Accepted" 
    REJECTED = "Rejected" 
    UNKNOWN_COMPONENT = "UnknownComponent" 
    UNKNOWN_VARIABLE = "UnknownVariable" 
    NOT_SUPPORTED_ATTRIBUTE_TYPE = "NotSupportedAttributeType" 
    REBOOT_REQUIRED = "RebootRequired" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    