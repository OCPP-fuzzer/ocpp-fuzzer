from type.IdTagInfo import IdTagInfo

class StartTransactionResponse:

    def __init__(self, idTagInfo: IdTagInfo, transactionId: int):
        self.idTagInfo = idTagInfo
        self.transactionId = transactionId

    def get_value(self):
        result = {
            "idTagInfo" : self.idTagInfo.get_value(),
            "transactionId" : self.transactionId,
        }
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['idTagInfo'] = IdTagInfo.get_sample(option=option)
        result['transactionId'] = 1
        return result