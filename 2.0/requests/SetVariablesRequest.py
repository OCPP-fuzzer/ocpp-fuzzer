from typing import List

from ocpptypes.SetVariableDataType import SetVariableDataType


class SetVariablesRequest:
    def __init__(self, setVariableData: List[SetVariableDataType]):
        self.setVariableData = setVariableData

    def to_dict(self):
        request = {
            "setVariableData" : [setVariableData.to_dict() for setVariableData in self.setVariableData],
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['setVariableData'] = [SetVariableDataType.sample(option=option)]

        return result
    