from typing import Optional

from type.DataTransferStatus import DataTransferStatus

class DataTransferResponse:

    def __init__(self, status: DataTransferStatus, data: Optional[str]= None):
        self.status = status
        if data:
            self.data = data

    def get_value(self):
        result = {
            "status" : self.status.get_value(),
        }
        if self.data:
            result['data'] = self.data
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['status'] = DataTransferStatus.get_sample(option=option)
        if option:
            result['data'] = "string"
        return result