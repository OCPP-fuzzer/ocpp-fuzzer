identifierString = str

class CostUpdatedRequest:
    def __init__(self, totalCost: float, transactionId: identifierString):
        self.totalCost = totalCost
        self.transactionId = transactionId

    def to_dict(self):
        request = {
            "totalCost" : self.totalCost,
            "transactionId" : self.transactionId,
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['totalCost'] = 1.0
        result['transactionId'] = str(__import__('uuid').uuid4())

        return result
    