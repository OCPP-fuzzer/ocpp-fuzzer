from typing import List, Optional

from ocppenum.PublishFirmwareStatusEnumType import PublishFirmwareStatusEnumType


class PublishFirmwareStatusNotificationRequest:
    def __init__(self, status: PublishFirmwareStatusEnumType, location: Optional[List[str]] = None, requestId: Optional[int] = None):
        self.status = status

        if location:
            self.location = location
        if requestId:
            self.requestId = requestId

    def to_dict(self):
        request = {
            "status" : self.status.value,
        }

        if self.location:
            request["location"] = [location for location in self.location]
        if self.requestId:
            request["requestId"] = self.requestId

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['status'] = PublishFirmwareStatusEnumType.sample()

        if option:
            result['location'] = ["string"]
            result['requestId'] = 1

        return result
    