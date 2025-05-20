from typing import Optional


class UnitOfMeasureType:
    def __init__(self, unit: Optional[str] = None, multiplier: Optional[int] = None):

        if unit:
            self.unit = unit
        if multiplier:
            self.multiplier = multiplier

    def to_dict(self):
        request = {
        }

        if self.unit:
            request["unit"] = self.unit
        if self.multiplier:
            request["multiplier"] = self.multiplier

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        if option:
            result['unit'] = "string"
            result['multiplier'] = 1

        return result
    