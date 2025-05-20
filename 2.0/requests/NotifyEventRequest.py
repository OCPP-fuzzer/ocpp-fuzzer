from typing import List, Optional

from datetime import datetime

from ocpptypes.EventDataType import EventDataType


class NotifyEventRequest:
    def __init__(self, generatedAt: datetime, seqNo: int, eventData: List[EventDataType], tbc: Optional[bool] = None):
        self.generatedAt = generatedAt
        self.seqNo = seqNo
        self.eventData = eventData

        if tbc:
            self.tbc = tbc

    def to_dict(self):
        request = {
            "generatedAt" : self.generatedAt.isoformat().split('.')[0] + 'Z',
            "seqNo" : self.seqNo,
            "eventData" : [eventData.to_dict() for eventData in self.eventData],
        }

        if self.tbc:
            request["tbc"] = self.tbc

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['generatedAt'] = datetime.now().isoformat().split('.')[0] + 'Z'
        result['seqNo'] = 1
        result['eventData'] = [EventDataType.sample(option=option)]

        if option:
            result['tbc'] = True

        return result
    