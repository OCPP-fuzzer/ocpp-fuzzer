from typing import Optional

from ocppenum.UploadLogStatusEnumType import UploadLogStatusEnumType


class LogStatusNotificationRequest:
    def __init__(self, status: UploadLogStatusEnumType, requestId: Optional[int] = None):
        self.status = status

        if requestId:
            self.requestId = requestId

    def to_dict(self):
        request = {
            "status" : self.status.value,
        }

        if self.requestId:
            request["requestId"] = self.requestId

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['status'] = UploadLogStatusEnumType.sample()

        if option:
            result['requestId'] = 1

        return result
    