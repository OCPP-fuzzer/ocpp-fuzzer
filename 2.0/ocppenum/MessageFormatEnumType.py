from enum import Enum
    
class MessageFormatEnumType(Enum):
    ASCII = "ASCII" 
    HTML = "HTML" 
    URI = "URI" 
    UTF8 = "UTF8" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    