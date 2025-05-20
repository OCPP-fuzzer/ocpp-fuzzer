from enum import Enum
    
class IdTokenEnumType(Enum):
    CENTRAL = "Central" 
    EMAID = "eMAID" 
    ISO14443 = "ISO14443" 
    ISO15693 = "ISO15693" 
    KEY_CODE = "KeyCode" 
    LOCAL = "Local" 
    MAC_ADDRESS = "MacAddress" 
    NO_AUTHORIZATION = "NoAuthorization" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    