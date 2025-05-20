from typing import Optional

from ocpptypes.IdTokenInfoType import IdTokenInfoType
from ocpptypes.IdTokenType import IdTokenType


class AuthorizationData:
    def __init__(self, idToken: IdTokenType, idTokenInfo: Optional[IdTokenInfoType] = None):
        self.idToken = idToken

        if idTokenInfo:
            self.idTokenInfo = idTokenInfo

    def to_dict(self):
        request = {
            "idToken" : self.idToken.to_dict(),
        }

        if self.idTokenInfo:
            request["idTokenInfo"] = self.idTokenInfo.to_dict()

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['idToken'] = IdTokenType.sample(option=option)

        if option:
            result['idTokenInfo'] = IdTokenInfoType.sample(option=option)

        return result
    