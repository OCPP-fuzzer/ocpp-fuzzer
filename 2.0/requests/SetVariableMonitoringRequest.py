from typing import List

from ocpptypes.SetMonitoringDataType import SetMonitoringDataType


class SetVariableMonitoringRequest:
    def __init__(self, setMonitoringData: List[SetMonitoringDataType]):
        self.setMonitoringData = setMonitoringData

    def to_dict(self):
        request = {
            "setMonitoringData" : [setMonitoringData.to_dict() for setMonitoringData in self.setMonitoringData],
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['setMonitoringData'] = [SetMonitoringDataType.sample(option=option)]

        return result
    