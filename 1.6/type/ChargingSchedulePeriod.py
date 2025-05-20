from typing import Optional

class ChargingSchedulePeriod:

    def __init__(self, startPeriod: int, limit: float, numberPhases: Optional[int]= None):
        self.startPeriod = startPeriod
        self.limit = limit
        if numberPhases:
            self.numberPhases = numberPhases

    def get_value(self):
        result = {
            "startPeriod" : self.startPeriod,
            "limit" : self.limit,
        }
        if self.numberPhases:
            result['numberPhases'] = self.numberPhases
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['startPeriod'] = 1
        result['limit'] = 1.0
        if option:
            result['numberPhases'] = 1
        return result