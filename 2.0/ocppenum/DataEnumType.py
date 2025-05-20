from enum import Enum
    
class DataEnumType(Enum):
    STRING = "string" 
    DECIMAL = "decimal" 
    INTEGER = "integer" 
    DATETIME = "dateTime" 
    BOOLEAN = "boolean" 
    OPTION_LIST = "OptionList" 
    SEQUENCE_LIST = "SequenceList" 
    MEMBER_LIST = "MemberList" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    