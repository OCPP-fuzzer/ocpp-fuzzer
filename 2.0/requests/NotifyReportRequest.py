from typing import Optional

from datetime import datetime


class NotifyReportRequest:
    def __init__(self, requestId: int, generatedAt: datetime, seqNo: int, tbc: Optional[bool] = None):
        self.requestId = requestId
        self.generatedAt = generatedAt
        self.seqNo = seqNo

        if tbc:
            self.tbc = tbc

    def to_dict(self):
        request = {
            "requestId" : self.requestId,
            "generatedAt" : self.generatedAt.isoformat().split('.')[0] + 'Z',
            "seqNo" : self.seqNo,
        }

        if self.tbc:
            request["tbc"] = self.tbc

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['requestId'] = 1
        result['generatedAt'] = datetime.now().isoformat().split('.')[0] + 'Z'
        result['seqNo'] = 1

        if option:
            result['tbc'] = True

        return result
    