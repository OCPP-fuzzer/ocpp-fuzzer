from typing import Optional

from ocppenum.ChargingLimitSourceEnumType import ChargingLimitSourceEnumType


class ClearedChargingLimitRequest:
    def __init__(self, chargingLimitSource: ChargingLimitSourceEnumType, evseId: Optional[int] = None):
        self.chargingLimitSource = chargingLimitSource

        if evseId:
            self.evseId = evseId

    def to_dict(self):
        request = {
            "chargingLimitSource" : self.chargingLimitSource.value,
        }

        if self.evseId:
            request["evseId"] = self.evseId

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['chargingLimitSource'] = ChargingLimitSourceEnumType.sample()

        if option:
            result['evseId'] = 1

        return result
    