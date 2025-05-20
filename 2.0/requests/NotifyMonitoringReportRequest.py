from typing import List, Optional

from datetime import datetime

from ocpptypes.MonitoringDataType import MonitoringDataType


class NotifyMonitoringReportRequest:
    def __init__(self, requestId: int, seqNo: int, generatedAt: datetime, tbc: Optional[bool] = None, monitor: Optional[List[MonitoringDataType]] = None):
        self.requestId = requestId
        self.seqNo = seqNo
        self.generatedAt = generatedAt

        if tbc:
            self.tbc = tbc
        if monitor:
            self.monitor = monitor

    def to_dict(self):
        request = {
            "requestId" : self.requestId,
            "seqNo" : self.seqNo,
            "generatedAt" : self.generatedAt.isoformat().split('.')[0] + 'Z',
        }

        if self.tbc:
            request["tbc"] = self.tbc
        if self.monitor:
            request["monitor"] = [monitor.to_dict() for monitor in self.monitor]

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['requestId'] = 1
        result['seqNo'] = 1
        result['generatedAt'] = datetime.now().isoformat().split('.')[0] + 'Z'

        if option:
            result['tbc'] = True
            result['monitor'] = [MonitoringDataType.sample(option=option)]

        return result
    