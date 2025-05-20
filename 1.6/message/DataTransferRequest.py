from typing import Optional

from type.CiString50Type import CiString50Type
from type.CiString255Type import CiString255Type

class DataTransferRequest:

    def __init__(self, vendorId: CiString255Type, messageId: Optional[CiString50Type]= None, data: Optional[str]= None):
        self.vendorId = vendorId
        if messageId:
            self.messageId = messageId
        if data:
            self.data = data

    def get_value(self):
        result = {
            "vendorId" : self.vendorId.get_value(),
        }
        if self.messageId:
            result['messageId'] = self.messageId.get_value()
        if self.data:
            result['data'] = self.data
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['vendorId'] = CiString255Type.get_sample(option=option)
        if option:
            result['messageId'] = CiString50Type.get_sample(option=option)
        if option:
            result['data'] = "string"
        return result