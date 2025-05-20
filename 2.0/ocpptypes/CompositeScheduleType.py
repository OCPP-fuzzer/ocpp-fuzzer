from typing import List

from datetime import datetime

from ocppenum.ChargingRateUnitEnumType import ChargingRateUnitEnumType
from ocpptypes.ChargingSchedulePeriodType import ChargingSchedulePeriodType


class CompositeScheduleType:
    def __init__(self, evseId: int, duration: int, scheduleStart: datetime, chargingRateUnit: ChargingRateUnitEnumType, chargingSchedulePeriod: List[ChargingSchedulePeriodType]):
        self.evseId = evseId
        self.duration = duration
        self.scheduleStart = scheduleStart
        self.chargingRateUnit = chargingRateUnit
        self.chargingSchedulePeriod = chargingSchedulePeriod

    def to_dict(self):
        request = {
            "evseId" : self.evseId,
            "duration" : self.duration,
            "scheduleStart" : self.scheduleStart.isoformat().split('.')[0] + 'Z',
            "chargingRateUnit" : self.chargingRateUnit.value,
            "chargingSchedulePeriod" : [chargingSchedulePeriod.to_dict() for chargingSchedulePeriod in self.chargingSchedulePeriod],
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['evseId'] = 1
        result['duration'] = 1
        result['scheduleStart'] = datetime.now().isoformat().split('.')[0] + 'Z'
        result['chargingRateUnit'] = ChargingRateUnitEnumType.sample()
        result['chargingSchedulePeriod'] = [ChargingSchedulePeriodType.sample(option=option)]

        return result
    