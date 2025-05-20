from datetime import datetime

from typing import Optional

from type.CiString50Type import CiString50Type
from type.ChargePointErrorCode import ChargePointErrorCode
from type.CiString255Type import CiString255Type
from type.ChargePointStatus import ChargePointStatus

class StatusNotificationRequest:

    def __init__(self,
        connectorId: int,
        errorCode: ChargePointErrorCode,
        status: ChargePointStatus,
        info: Optional[CiString50Type]= None,
        timestamp: Optional[datetime]= None,
        vendorId: Optional[CiString255Type]= None,
        vendorErrorCode: Optional[CiString50Type]= None
    ):
        self.connectorId = connectorId
        self.errorCode = errorCode
        self.status = status
        if info:
            self.info = info
        if timestamp:
            self.timestamp = timestamp
        if vendorId:
            self.vendorId = vendorId
        if vendorErrorCode:
            self.vendorErrorCode = vendorErrorCode

    def get_value(self):
        result = {
            "connectorId" : self.connectorId,
            "errorCode" : self.errorCode.get_value(),
            "status" : self.status.get_value(),
        }
        if self.info:
            result['info'] = self.info.get_value()
        if self.timestamp:
            result['timestamp'] = self.timestamp.isoformat().split('.')[0] + 'Z'
        if self.vendorId:
            result['vendorId'] = self.vendorId.get_value()
        if self.vendorErrorCode:
            result['vendorErrorCode'] = self.vendorErrorCode.get_value()
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['connectorId'] = 1
        result['errorCode'] = ChargePointErrorCode.get_sample(option=option)
        result['status'] = ChargePointStatus.get_sample(option=option)
        if option:
            result['info'] = CiString50Type.get_sample(option=option)
        if option:
            result['timestamp'] = datetime.now().isoformat().split('.')[0] + 'Z'
        if option:
            result['vendorId'] = CiString255Type.get_sample(option=option)
        if option:
            result['vendorErrorCode'] = CiString50Type.get_sample(option=option)
        return result