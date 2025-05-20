from typing import Optional

from type.IdToken import IdToken
from type.IdTagInfo import IdTagInfo

class AuthorizationData:

    def __init__(self, idTag: IdToken, idTagInfo: Optional[IdTagInfo]= None):
        self.idTag = idTag
        if idTagInfo:
            self.idTagInfo = idTagInfo

    def get_value(self):
        result = {
            "idTag" : self.idTag.get_value(),
        }
        if self.idTagInfo:
            result['idTagInfo'] = self.idTagInfo.get_value()
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['idTag'] = IdToken.get_sample(option=option)
        if option:
            result['idTagInfo'] = IdTagInfo.get_sample(option=option)
        return result