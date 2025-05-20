from typing import List, Optional

from ocpptypes.MessageInfoType import MessageInfoType


class NotifyDisplayMessagesRequest:
    def __init__(self, requestId: int, tbc: Optional[bool] = None, messageInfo: Optional[List[MessageInfoType]] = None):
        self.requestId = requestId

        if tbc:
            self.tbc = tbc
        if messageInfo:
            self.messageInfo = messageInfo

    def to_dict(self):
        request = {
            "requestId" : self.requestId,
        }

        if self.tbc:
            request["tbc"] = self.tbc
        if self.messageInfo:
            request["messageInfo"] = [messageInfo.to_dict() for messageInfo in self.messageInfo]

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['requestId'] = 1

        if option:
            result['tbc'] = True
            result['messageInfo'] = [MessageInfoType.sample(option=option)]

        return result
    