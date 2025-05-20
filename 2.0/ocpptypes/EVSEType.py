from typing import Optional


class EVSEType:
    def __init__(self, id: int, connectorId: Optional[int] = None):
        self.id = id

        if connectorId:
            self.connectorId = connectorId

    def to_dict(self):
        request = {
            "id" : self.id,
        }

        if self.connectorId:
            request["connectorId"] = self.connectorId

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['id'] = 1

        if option:
            result['connectorId'] = 1

        return result
    