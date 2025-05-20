from typing import Optional

from ocppenum.ClearMonitoringStatusEnumType import ClearMonitoringStatusEnumType
from ocpptypes.StatusInfoType import StatusInfoType


class ClearMonitoringResultType:
    def __init__(self, status: ClearMonitoringStatusEnumType, id: int, statusInfo: Optional[StatusInfoType] = None):
        self.status = status
        self.id = id

        if statusInfo:
            self.statusInfo = statusInfo

    def to_dict(self):
        request = {
            "status" : self.status.value,
            "id" : self.id,
        }

        if self.statusInfo:
            request["statusInfo"] = self.statusInfo.to_dict()

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['status'] = ClearMonitoringStatusEnumType.sample()
        result['id'] = 1

        if option:
            result['statusInfo'] = StatusInfoType.sample(option=option)

        return result
    