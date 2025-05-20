from enum import Enum
    
class UnlockStatusEnumType(Enum):
    UNLOCKED = "Unlocked" 
    UNLOCK_FAILED = "UnlockFailed" 
    ONGOING_AUTHORIZED_TRANSACTION = "OngoingAuthorizedTransaction" 
    UNKNOWN_CONNECTOR = "UnknownConnector" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    