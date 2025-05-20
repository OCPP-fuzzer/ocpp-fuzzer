
class RemoteStopTransactionRequest:

    def __init__(self, transactionId: int):
        self.transactionId = transactionId

    def get_value(self):
        result = {
            "transactionId" : self.transactionId,
        }
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['transactionId'] = 1
        return result