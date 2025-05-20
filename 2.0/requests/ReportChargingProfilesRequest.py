from typing import List, Optional

from ocppenum.ChargingLimitSourceEnumType import ChargingLimitSourceEnumType
from ocpptypes.ChargingProfileType import ChargingProfileType


class ReportChargingProfilesRequest:
    def __init__(self, requestId: int, chargingLimitSource: ChargingLimitSourceEnumType, evseId: int, chargingProfile: List[ChargingProfileType], tbc: Optional[bool] = None):
        self.requestId = requestId
        self.chargingLimitSource = chargingLimitSource
        self.evseId = evseId
        self.chargingProfile = chargingProfile

        if tbc:
            self.tbc = tbc

    def to_dict(self):
        request = {
            "requestId" : self.requestId,
            "chargingLimitSource" : self.chargingLimitSource.value,
            "evseId" : self.evseId,
            "chargingProfile" : [chargingProfile.to_dict() for chargingProfile in self.chargingProfile],
        }

        if self.tbc:
            request["tbc"] = self.tbc

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['requestId'] = 1
        result['chargingLimitSource'] = ChargingLimitSourceEnumType.sample()
        result['evseId'] = 1
        result['chargingProfile'] = [ChargingProfileType.sample(option=option)]

        if option:
            result['tbc'] = True

        return result
    