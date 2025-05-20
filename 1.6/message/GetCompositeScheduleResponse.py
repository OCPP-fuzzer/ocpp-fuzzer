from datetime import datetime

from typing import Optional

from type.ChargingSchedule import ChargingSchedule
from type.GetCompositeScheduleStatus import GetCompositeScheduleStatus

class GetCompositeScheduleResponse:

    def __init__(self,
        status: GetCompositeScheduleStatus,
        connectorId: Optional[int]= None,
        scheduleStart: Optional[datetime]= None,
        chargingSchedule: Optional[ChargingSchedule]= None
    ):
        self.status = status
        if connectorId:
            self.connectorId = connectorId
        if scheduleStart:
            self.scheduleStart = scheduleStart
        if chargingSchedule:
            self.chargingSchedule = chargingSchedule

    def get_value(self):
        result = {
            "status" : self.status.get_value(),
        }
        if self.connectorId:
            result['connectorId'] = self.connectorId
        if self.scheduleStart:
            result['scheduleStart'] = self.scheduleStart.isoformat().split('.')[0] + 'Z'
        if self.chargingSchedule:
            result['chargingSchedule'] = self.chargingSchedule.get_value()
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['status'] = GetCompositeScheduleStatus.get_sample(option=option)
        if option:
            result['connectorId'] = 1
        if option:
            result['scheduleStart'] = datetime.now().isoformat().split('.')[0] + 'Z'
        if option:
            result['chargingSchedule'] = ChargingSchedule.get_sample(option=option)
        return result