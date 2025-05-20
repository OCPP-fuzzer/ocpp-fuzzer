from typing import List

from ocpptypes.CostType import CostType


class ConsumptionCostType:
    def __init__(self, startValue: float, cost: List[CostType]):
        self.startValue = startValue
        self.cost = cost

    def to_dict(self):
        request = {
            "startValue" : self.startValue,
            "cost" : [cost.to_dict() for cost in self.cost],
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['startValue'] = 1.0
        result['cost'] = [CostType.sample(option=option)]

        return result
    