from datetime import datetime

from typing import List, Optional

from type.ChargingSchedulePeriod import ChargingSchedulePeriod
from type.ChargingRateUnitType import ChargingRateUnitType

class ChargingSchedule:

    def __init__(self,
        chargingRateUnit: ChargingRateUnitType,
        chargingSchedulePeriod: List[ChargingSchedulePeriod],
        duration: Optional[int]= None,
        startSchedule: Optional[datetime]= None,
        minChargingRate: Optional[float]= None
    ):
        self.chargingRateUnit = chargingRateUnit
        self.chargingSchedulePeriod = chargingSchedulePeriod
        if duration:
            self.duration = duration
        if startSchedule:
            self.startSchedule = startSchedule
        if minChargingRate:
            self.minChargingRate = minChargingRate

    def get_value(self):
        result = {
            "chargingRateUnit" : self.chargingRateUnit.get_value(),
            "chargingSchedulePeriod" : [ chargingSchedulePeriod.get_value() for chargingSchedulePeriod in self.chargingSchedulePeriod ],
        }
        if self.duration:
            result['duration'] = self.duration
        if self.startSchedule:
            result['startSchedule'] = self.startSchedule.isoformat().split('.')[0] + 'Z'
        if self.minChargingRate:
            result['minChargingRate'] = self.minChargingRate
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['chargingRateUnit'] = ChargingRateUnitType.get_sample(option=option)
        result['chargingSchedulePeriod'] = [ ChargingSchedulePeriod.get_sample(option=option), ]
        if option:
            result['duration'] = 1
        if option:
            result['startSchedule'] = datetime.now().isoformat().split('.')[0] + 'Z'
        if option:
            result['minChargingRate'] = 1.0
        return result