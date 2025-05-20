from typing import List

from ocpptypes.GetVariableDataType import GetVariableDataType


class GetVariablesRequest:
    def __init__(self, getVariableData: List[GetVariableDataType]):
        self.getVariableData = getVariableData

    def to_dict(self):
        request = {
            "getVariableData" : [getVariableData.to_dict() for getVariableData in self.getVariableData],
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['getVariableData'] = [GetVariableDataType.sample(option=option)]

        return result
    