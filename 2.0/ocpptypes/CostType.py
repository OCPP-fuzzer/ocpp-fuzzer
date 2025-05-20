from typing import Optional

from ocppenum.CostKindEnumType import CostKindEnumType


class CostType:
    def __init__(self, costKind: CostKindEnumType, amount: int, amountMultiplier: Optional[int] = None):
        self.costKind = costKind
        self.amount = amount

        if amountMultiplier:
            self.amountMultiplier = amountMultiplier

    def to_dict(self):
        request = {
            "costKind" : self.costKind.value,
            "amount" : self.amount,
        }

        if self.amountMultiplier:
            request["amountMultiplier"] = self.amountMultiplier

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['costKind'] = CostKindEnumType.sample()
        result['amount'] = 1

        if option:
            result['amountMultiplier'] = 1

        return result
    