from typing import Optional

from type.ChargingProfilePurposeType import ChargingProfilePurposeType

class ClearChargingProfileRequest:

    def __init__(self,
        id: Optional[int]= None,
        connectorId: Optional[int]= None,
        chargingProfilePurpose: Optional[ChargingProfilePurposeType]= None,
        stackLevel: Optional[int]= None
    ):
        if id:
            self.id = id
        if connectorId:
            self.connectorId = connectorId
        if chargingProfilePurpose:
            self.chargingProfilePurpose = chargingProfilePurpose
        if stackLevel:
            self.stackLevel = stackLevel

    def get_value(self):
        result = {
        }
        if self.id:
            result['id'] = self.id
        if self.connectorId:
            result['connectorId'] = self.connectorId
        if self.chargingProfilePurpose:
            result['chargingProfilePurpose'] = self.chargingProfilePurpose.get_value()
        if self.stackLevel:
            result['stackLevel'] = self.stackLevel
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        if option:
            result['id'] = 1
        if option:
            result['connectorId'] = 1
        if option:
            result['chargingProfilePurpose'] = ChargingProfilePurposeType.get_sample(option=option)
        if option:
            result['stackLevel'] = 1
        return result