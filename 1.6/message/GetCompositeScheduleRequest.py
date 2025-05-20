from typing import Optional

from type.ChargingRateUnitType import ChargingRateUnitType

class GetCompositeScheduleRequest:

    def __init__(self, connectorId: int, duration: int, chargingRateUnit: Optional[ChargingRateUnitType]= None):
        self.connectorId = connectorId
        self.duration = duration
        if chargingRateUnit:
            self.chargingRateUnit = chargingRateUnit

    def get_value(self):
        result = {
            "connectorId" : self.connectorId,
            "duration" : self.duration,
        }
        if self.chargingRateUnit:
            result['chargingRateUnit'] = self.chargingRateUnit.get_value()
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['connectorId'] = 1
        result['duration'] = 1
        if option:
            result['chargingRateUnit'] = ChargingRateUnitType.get_sample(option=option)
        return result