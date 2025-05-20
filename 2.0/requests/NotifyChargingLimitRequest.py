from typing import List, Optional

from ocpptypes.ChargingLimitType import ChargingLimitType
from ocpptypes.ChargingScheduleType import ChargingScheduleType


class NotifyChargingLimitRequest:
    def __init__(self, chargingLimit: ChargingLimitType, evseId: Optional[int] = None, chargingSchedule: Optional[List[ChargingScheduleType]] = None):
        self.chargingLimit = chargingLimit

        if evseId:
            self.evseId = evseId
        if chargingSchedule:
            self.chargingSchedule = chargingSchedule

    def to_dict(self):
        request = {
            "chargingLimit" : self.chargingLimit.to_dict(),
        }

        if self.evseId:
            request["evseId"] = self.evseId
        if self.chargingSchedule:
            request["chargingSchedule"] = [chargingSchedule.to_dict() for chargingSchedule in self.chargingSchedule]

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['chargingLimit'] = ChargingLimitType.sample(option=option)

        if option:
            result['evseId'] = 1
            result['chargingSchedule'] = [ChargingScheduleType.sample(option=option)]

        return result
    