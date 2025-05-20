from typing import Optional, List

from ocpptypes.RelativeTimeIntervalType import RelativeTimeIntervalType
from ocpptypes.ConsumptionCostType import ConsumptionCostType


class SalesTariffEntryType:
    def __init__(self, relativeTimeInterval: RelativeTimeIntervalType, ePriceLevel: Optional[int] = None, consumptionCost: Optional[List[ConsumptionCostType]] = None):
        self.relativeTimeInterval = relativeTimeInterval

        if ePriceLevel:
            self.ePriceLevel = ePriceLevel
        if consumptionCost:
            self.consumptionCost = consumptionCost

    def to_dict(self):
        request = {
            "relativeTimeInterval" : self.relativeTimeInterval.to_dict(),
        }

        if self.ePriceLevel:
            request["ePriceLevel"] = self.ePriceLevel
        if self.consumptionCost:
            request["consumptionCost"] = [consumptionCost.to_dict() for consumptionCost in self.consumptionCost]

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['relativeTimeInterval'] = RelativeTimeIntervalType.sample(option=option)

        if option:
            result['ePriceLevel'] = 1
            result['consumptionCost'] = [ConsumptionCostType.sample(option=option)]

        return result
    