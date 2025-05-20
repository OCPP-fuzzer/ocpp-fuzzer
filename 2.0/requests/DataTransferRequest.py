from typing import Optional, Any


class DataTransferRequest:
    def __init__(self, vendorId: str, messageId: Optional[str] = None, data: Optional[Any] = None):
        self.vendorId = vendorId

        if messageId:
            self.messageId = messageId
        if data:
            self.data = data

    def to_dict(self):
        request = {
            "vendorId" : self.vendorId,
        }

        if self.messageId:
            request["messageId"] = self.messageId
        if self.data:
            request["data"] = self.data

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['vendorId'] = "string"

        if option:
            result['messageId'] = "string"
            result['data'] = None

        return result
    