from enum import Enum
    
class ReadingContextEnumType(Enum):
    INTERRUPTION__BEGIN = "Interruption.Begin" 
    INTERRUPTION__END = "Interruption.End" 
    OTHER = "Other" 
    SAMPLE__CLOCK = "Sample.Clock" 
    SAMPLE__PERIODIC = "Sample.Periodic" 
    TRANSACTION__BEGIN = "Transaction.Begin" 
    TRANSACTION__END = "Transaction.End" 
    TRIGGER = "Trigger" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    