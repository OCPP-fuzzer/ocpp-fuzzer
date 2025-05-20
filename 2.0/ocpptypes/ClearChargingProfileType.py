from typing import Optional

from ocppenum.ChargingProfilePurposeEnumType import ChargingProfilePurposeEnumType


class ClearChargingProfileType:
    def __init__(self, evseId: Optional[int] = None, chargingProfilePurpose: Optional[ChargingProfilePurposeEnumType] = None, stackLevel: Optional[int] = None):

        if evseId:
            self.evseId = evseId
        if chargingProfilePurpose:
            self.chargingProfilePurpose = chargingProfilePurpose
        if stackLevel:
            self.stackLevel = stackLevel

    def to_dict(self):
        request = {
        }

        if self.evseId:
            request["evseId"] = self.evseId
        if self.chargingProfilePurpose:
            request["chargingProfilePurpose"] = self.chargingProfilePurpose.value
        if self.stackLevel:
            request["stackLevel"] = self.stackLevel

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        if option:
            result['evseId'] = 1
            result['chargingProfilePurpose'] = ChargingProfilePurposeEnumType.sample()
            result['stackLevel'] = 1

        return result
    