identifierString = str

class AdditionalInfoType:
    def __init__(self, additionalIdToken: identifierString, type: str):
        self.additionalIdToken = additionalIdToken
        self.type = type

    def to_dict(self):
        request = {
            "additionalIdToken" : self.additionalIdToken,
            "type" : self.type,
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['additionalIdToken'] = str(__import__('uuid').uuid4())
        result['type'] = "string"

        return result
    