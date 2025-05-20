from enum import Enum
    
class LogEnumType(Enum):
    DIAGNOSTICS_LOG = "DiagnosticsLog" 
    SECURITY_LOG = "SecurityLog" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    