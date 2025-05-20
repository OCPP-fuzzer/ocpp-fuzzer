from type.IdToken import IdToken

class AuthorizeRequest:

    def __init__(self, idTag: IdToken):
        self.idTag = idTag

    def get_value(self):
        result = {
            "idTag" : self.idTag.get_value(),
        }
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['idTag'] = IdToken.get_sample(option=option)
        return result