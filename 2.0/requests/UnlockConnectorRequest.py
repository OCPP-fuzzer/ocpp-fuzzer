
class UnlockConnectorRequest:
    def __init__(self, evseId: int, connectorId: int):
        self.evseId = evseId
        self.connectorId = connectorId

    def to_dict(self):
        request = {
            "evseId" : self.evseId,
            "connectorId" : self.connectorId,
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['evseId'] = 1
        result['connectorId'] = 1

        return result
    