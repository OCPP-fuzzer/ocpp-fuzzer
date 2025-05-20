identifierString = str

class RequestStopTransactionRequest:
    def __init__(self, transactionId: identifierString):
        self.transactionId = transactionId

    def to_dict(self):
        request = {
            "transactionId" : self.transactionId,
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['transactionId'] = str(__import__('uuid').uuid4())

        return result
    