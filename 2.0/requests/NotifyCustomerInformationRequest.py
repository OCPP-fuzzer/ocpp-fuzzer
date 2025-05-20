from typing import Optional

from datetime import datetime


class NotifyCustomerInformationRequest:
    def __init__(self, data: str, seqNo: int, generatedAt: datetime, requestId: int, tbc: Optional[bool] = None):
        self.data = data
        self.seqNo = seqNo
        self.generatedAt = generatedAt
        self.requestId = requestId

        if tbc:
            self.tbc = tbc

    def to_dict(self):
        request = {
            "data" : self.data,
            "seqNo" : self.seqNo,
            "generatedAt" : self.generatedAt.isoformat().split('.')[0] + 'Z',
            "requestId" : self.requestId,
        }

        if self.tbc:
            request["tbc"] = self.tbc

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['data'] = "string"
        result['seqNo'] = 1
        result['generatedAt'] = datetime.now().isoformat().split('.')[0] + 'Z'
        result['requestId'] = 1

        if option:
            result['tbc'] = True

        return result
    