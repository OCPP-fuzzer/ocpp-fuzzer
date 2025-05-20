from typing import Optional, List

from datetime import datetime

from ocppenum.ChargingRateUnitEnumType import ChargingRateUnitEnumType
from ocpptypes.ChargingSchedulePeriodType import ChargingSchedulePeriodType
from ocpptypes.SalesTariffType import SalesTariffType


class ChargingScheduleType:
    def __init__(self, id: int, chargingRateUnit: ChargingRateUnitEnumType, chargingSchedulePeriod: List[ChargingSchedulePeriodType], startSchedule: Optional[datetime] = None, duration: Optional[int] = None, minChargingRate: Optional[float] = None, salesTariff: Optional[SalesTariffType] = None):
        self.id = id
        self.chargingRateUnit = chargingRateUnit
        self.chargingSchedulePeriod = chargingSchedulePeriod

        if startSchedule:
            self.startSchedule = startSchedule
        if duration:
            self.duration = duration
        if minChargingRate:
            self.minChargingRate = minChargingRate
        if salesTariff:
            self.salesTariff = salesTariff

    def to_dict(self):
        request = {
            "id" : self.id,
            "chargingRateUnit" : self.chargingRateUnit.value,
            "chargingSchedulePeriod" : [chargingSchedulePeriod.to_dict() for chargingSchedulePeriod in self.chargingSchedulePeriod],
        }

        if self.startSchedule:
            request["startSchedule"] = self.startSchedule.isoformat().split('.')[0] + 'Z'
        if self.duration:
            request["duration"] = self.duration
        if self.minChargingRate:
            request["minChargingRate"] = self.minChargingRate
        if self.salesTariff:
            request["salesTariff"] = self.salesTariff.to_dict()

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['id'] = 1
        result['chargingRateUnit'] = ChargingRateUnitEnumType.sample()
        result['chargingSchedulePeriod'] = [ChargingSchedulePeriodType.sample(option=option)]

        if option:
            result['startSchedule'] = datetime.now().isoformat().split('.')[0] + 'Z'
            result['duration'] = 1
            result['minChargingRate'] = 1.0
            result['salesTariff'] = SalesTariffType.sample(option=option)

        return result
    