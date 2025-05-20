from typing import Optional

from ocppenum.ChargingRateUnitEnumType import ChargingRateUnitEnumType


class GetCompositeScheduleRequest:
    def __init__(self, duration: int, evseId: int, chargingRateUnit: Optional[ChargingRateUnitEnumType] = None):
        self.duration = duration
        self.evseId = evseId

        if chargingRateUnit:
            self.chargingRateUnit = chargingRateUnit

    def to_dict(self):
        request = {
            "duration" : self.duration,
            "evseId" : self.evseId,
        }

        if self.chargingRateUnit:
            request["chargingRateUnit"] = self.chargingRateUnit.value

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['duration'] = 1
        result['evseId'] = 1

        if option:
            result['chargingRateUnit'] = ChargingRateUnitEnumType.sample()

        return result
    