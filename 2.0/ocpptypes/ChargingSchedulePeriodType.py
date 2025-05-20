from typing import Optional


class ChargingSchedulePeriodType:
    def __init__(self, startPeriod: int, limit: float, numberPhases: Optional[int] = None, phaseToUse: Optional[int] = None):
        self.startPeriod = startPeriod
        self.limit = limit

        if numberPhases:
            self.numberPhases = numberPhases
        if phaseToUse:
            self.phaseToUse = phaseToUse

    def to_dict(self):
        request = {
            "startPeriod" : self.startPeriod,
            "limit" : self.limit,
        }

        if self.numberPhases:
            request["numberPhases"] = self.numberPhases
        if self.phaseToUse:
            request["phaseToUse"] = self.phaseToUse

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['startPeriod'] = 1
        result['limit'] = 1.0

        if option:
            result['numberPhases'] = 1
            result['phaseToUse'] = 1

        return result
    