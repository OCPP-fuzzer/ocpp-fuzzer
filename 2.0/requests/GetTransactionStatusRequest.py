from typing import Optional

identifierString = str

class GetTransactionStatusRequest:
    def __init__(self, transactionId: Optional[identifierString] = None):

        if transactionId:
            self.transactionId = transactionId

    def to_dict(self):
        request = {
        }

        if self.transactionId:
            request["transactionId"] = self.transactionId

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        if option:
            result['transactionId'] = str(__import__('uuid').uuid4())

        return result
    