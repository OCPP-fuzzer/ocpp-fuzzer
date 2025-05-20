from typing import Optional

from ocpptypes.ClearChargingProfileType import ClearChargingProfileType


class ClearChargingProfileRequest:
    def __init__(self, chargingProfileId: Optional[int] = None, chargingProfileCriteria: Optional[ClearChargingProfileType] = None):

        if chargingProfileId:
            self.chargingProfileId = chargingProfileId
        if chargingProfileCriteria:
            self.chargingProfileCriteria = chargingProfileCriteria

    def to_dict(self):
        request = {
        }

        if self.chargingProfileId:
            request["chargingProfileId"] = self.chargingProfileId
        if self.chargingProfileCriteria:
            request["chargingProfileCriteria"] = self.chargingProfileCriteria.to_dict()

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        if option:
            result['chargingProfileId'] = 1
            result['chargingProfileCriteria'] = ClearChargingProfileType.sample(option=option)

        return result
    