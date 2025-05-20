from datetime import datetime

from ocpptypes.ChargingScheduleType import ChargingScheduleType


class NotifyEVChargingScheduleRequest:
    def __init__(self, timeBase: datetime, evseId: int, chargingSchedule: ChargingScheduleType):
        self.timeBase = timeBase
        self.evseId = evseId
        self.chargingSchedule = chargingSchedule

    def to_dict(self):
        request = {
            "timeBase" : self.timeBase.isoformat().split('.')[0] + 'Z',
            "evseId" : self.evseId,
            "chargingSchedule" : self.chargingSchedule.to_dict(),
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['timeBase'] = datetime.now().isoformat().split('.')[0] + 'Z'
        result['evseId'] = 1
        result['chargingSchedule'] = ChargingScheduleType.sample(option=option)

        return result
    