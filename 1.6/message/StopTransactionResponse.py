from typing import Optional

from type.IdTagInfo import IdTagInfo

class StopTransactionResponse:

    def __init__(self, idTagInfo: Optional[IdTagInfo]= None):
        if idTagInfo:
            self.idTagInfo = idTagInfo

    def get_value(self):
        result = {
        }
        if self.idTagInfo:
            result['idTagInfo'] = self.idTagInfo.get_value()
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        if option:
            result['idTagInfo'] = IdTagInfo.get_sample(option=option)
        return result