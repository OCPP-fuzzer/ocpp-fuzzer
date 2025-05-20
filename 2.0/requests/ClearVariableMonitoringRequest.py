from typing import List


class ClearVariableMonitoringRequest:
    def __init__(self, id: List[int]):
        self.id = id

    def to_dict(self):
        request = {
            "id" : [id for id in self.id],
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['id'] = [1]

        return result
    