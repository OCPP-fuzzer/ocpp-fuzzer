from typing import Optional

from ocpptypes.ChargingNeedsType import ChargingNeedsType


class NotifyEVChargingNeedsRequest:
    def __init__(self, evseId: int, chargingNeeds: ChargingNeedsType, maxScheduleTuples: Optional[int] = None):
        self.evseId = evseId
        self.chargingNeeds = chargingNeeds

        if maxScheduleTuples:
            self.maxScheduleTuples = maxScheduleTuples

    def to_dict(self):
        request = {
            "evseId" : self.evseId,
            "chargingNeeds" : self.chargingNeeds.to_dict(),
        }

        if self.maxScheduleTuples:
            request["maxScheduleTuples"] = self.maxScheduleTuples

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['evseId'] = 1
        result['chargingNeeds'] = ChargingNeedsType.sample(option=option)

        if option:
            result['maxScheduleTuples'] = 1

        return result
    