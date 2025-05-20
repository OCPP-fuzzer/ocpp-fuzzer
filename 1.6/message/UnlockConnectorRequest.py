
class UnlockConnectorRequest:

    def __init__(self, connectorId: int):
        self.connectorId = connectorId

    def get_value(self):
        result = {
            "connectorId" : self.connectorId,
        }
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['connectorId'] = 1
        return result