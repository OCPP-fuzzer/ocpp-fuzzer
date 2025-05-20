from typing import Optional, List

from datetime import datetime

from ocppenum.AuthorizationStatusEnumType import AuthorizationStatusEnumType
from ocpptypes.IdTokenType import IdTokenType
from ocpptypes.MessageContentType import MessageContentType


class IdTokenInfoType:
    def __init__(self, status: AuthorizationStatusEnumType, cacheExpiryDateTime: Optional[datetime] = None, chargingPriority: Optional[int] = None, language1: Optional[str] = None, evseId: Optional[List[int]] = None, language2: Optional[str] = None, groupIdToken: Optional[IdTokenType] = None, personalMessage: Optional[MessageContentType] = None):
        self.status = status

        if cacheExpiryDateTime:
            self.cacheExpiryDateTime = cacheExpiryDateTime
        if chargingPriority:
            self.chargingPriority = chargingPriority
        if language1:
            self.language1 = language1
        if evseId:
            self.evseId = evseId
        if language2:
            self.language2 = language2
        if groupIdToken:
            self.groupIdToken = groupIdToken
        if personalMessage:
            self.personalMessage = personalMessage

    def to_dict(self):
        request = {
            "status" : self.status.value,
        }

        if self.cacheExpiryDateTime:
            request["cacheExpiryDateTime"] = self.cacheExpiryDateTime.isoformat().split('.')[0] + 'Z'
        if self.chargingPriority:
            request["chargingPriority"] = self.chargingPriority
        if self.language1:
            request["language1"] = self.language1
        if self.evseId:
            request["evseId"] = [evseId for evseId in self.evseId]
        if self.language2:
            request["language2"] = self.language2
        if self.groupIdToken:
            request["groupIdToken"] = self.groupIdToken.to_dict()
        if self.personalMessage:
            request["personalMessage"] = self.personalMessage.to_dict()

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['status'] = AuthorizationStatusEnumType.sample()

        if option:
            result['cacheExpiryDateTime'] = datetime.now().isoformat().split('.')[0] + 'Z'
            result['chargingPriority'] = 1
            result['language1'] = "string"
            result['evseId'] = [1]
            result['language2'] = "string"
            result['groupIdToken'] = IdTokenType.sample(option=option)
            result['personalMessage'] = MessageContentType.sample(option=option)

        return result
    