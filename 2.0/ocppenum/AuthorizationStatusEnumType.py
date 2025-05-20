from enum import Enum
    
class AuthorizationStatusEnumType(Enum):
    ACCEPTED = "Accepted" 
    BLOCKED = "Blocked" 
    CONCURRENT_TX = "ConcurrentTx" 
    EXPIRED = "Expired" 
    INVALID = "Invalid" 
    NO_CREDIT = "NoCredit" 
    NOT_ALLOWED_TYPE_E_V_S_E = "NotAllowedTypeEVSE" 
    NOT_AT_THIS_LOCATION = "NotAtThisLocation" 
    NOT_AT_THIS_TIME = "NotAtThisTime" 
    UNKNOWN = "Unknown" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    