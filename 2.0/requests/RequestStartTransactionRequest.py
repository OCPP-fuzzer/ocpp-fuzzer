from typing import Optional

from ocpptypes.IdTokenType import IdTokenType
from ocpptypes.ChargingProfileType import ChargingProfileType
from ocpptypes.IdTokenType import IdTokenType


class RequestStartTransactionRequest:
    def __init__(self, remoteStartId: int, idToken: IdTokenType, evseId: Optional[int] = None, chargingProfile: Optional[ChargingProfileType] = None, groupIdToken: Optional[IdTokenType] = None):
        self.remoteStartId = remoteStartId
        self.idToken = idToken

        if evseId:
            self.evseId = evseId
        if chargingProfile:
            self.chargingProfile = chargingProfile
        if groupIdToken:
            self.groupIdToken = groupIdToken

    def to_dict(self):
        request = {
            "remoteStartId" : self.remoteStartId,
            "idToken" : self.idToken.to_dict(),
        }

        if self.evseId:
            request["evseId"] = self.evseId
        if self.chargingProfile:
            request["chargingProfile"] = self.chargingProfile.to_dict()
        if self.groupIdToken:
            request["groupIdToken"] = self.groupIdToken.to_dict()

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['remoteStartId'] = 1
        result['idToken'] = IdTokenType.sample(option=option)

        if option:
            result['evseId'] = 1
            result['chargingProfile'] = ChargingProfileType.sample(option=option)
            result['groupIdToken'] = IdTokenType.sample(option=option)

        return result
    