from type.IdTagInfo import IdTagInfo

class AuthorizeResponse:

    def __init__(self, idTagInfo: IdTagInfo):
        self.idTagInfo = idTagInfo

    def get_value(self):
        result = {
            "idTagInfo" : self.idTagInfo.get_value(),
        }
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['idTagInfo'] = IdTagInfo.get_sample(option=option)
        return result