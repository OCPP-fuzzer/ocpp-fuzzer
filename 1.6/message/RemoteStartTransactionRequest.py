from typing import Optional

from type.ChargingProfile import ChargingProfile
from type.IdToken import IdToken

class RemoteStartTransactionRequest:

    def __init__(self, idTag: IdToken, connectorId: Optional[int]= None, chargingProfile: Optional[ChargingProfile]= None):
        self.idTag = idTag
        if connectorId:
            self.connectorId = connectorId
        if chargingProfile:
            self.chargingProfile = chargingProfile

    def get_value(self):
        result = {
            "idTag" : self.idTag.get_value(),
        }
        if self.connectorId:
            result['connectorId'] = self.connectorId
        if self.chargingProfile:
            result['chargingProfile'] = self.chargingProfile.get_value()
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['idTag'] = IdToken.get_sample(option=option)
        if option:
            result['connectorId'] = 1
        if option:
            result['chargingProfile'] = ChargingProfile.get_sample(option=option)
        return result