from typing import Optional

from ocpptypes.ChargingProfileCriterionType import ChargingProfileCriterionType


class GetChargingProfilesRequest:
    def __init__(self, requestId: int, chargingProfile: ChargingProfileCriterionType, evseId: Optional[int] = None):
        self.requestId = requestId
        self.chargingProfile = chargingProfile

        if evseId:
            self.evseId = evseId

    def to_dict(self):
        request = {
            "requestId" : self.requestId,
            "chargingProfile" : self.chargingProfile.to_dict(),
        }

        if self.evseId:
            request["evseId"] = self.evseId

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['requestId'] = 1
        result['chargingProfile'] = ChargingProfileCriterionType.sample(option=option)

        if option:
            result['evseId'] = 1

        return result
    