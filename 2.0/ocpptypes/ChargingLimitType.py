from typing import Optional

from ocppenum.ChargingLimitSourceEnumType import ChargingLimitSourceEnumType


class ChargingLimitType:
    def __init__(self, chargingLimitSource: ChargingLimitSourceEnumType, isGridCritical: Optional[bool] = None):
        self.chargingLimitSource = chargingLimitSource

        if isGridCritical:
            self.isGridCritical = isGridCritical

    def to_dict(self):
        request = {
            "chargingLimitSource" : self.chargingLimitSource.value,
        }

        if self.isGridCritical:
            request["isGridCritical"] = self.isGridCritical

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['chargingLimitSource'] = ChargingLimitSourceEnumType.sample()

        if option:
            result['isGridCritical'] = True

        return result
    