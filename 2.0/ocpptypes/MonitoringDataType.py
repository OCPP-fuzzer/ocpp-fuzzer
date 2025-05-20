from typing import List

from ocpptypes.ComponentType import ComponentType
from ocpptypes.VariableType import VariableType
from ocpptypes.VariableMonitoringType import VariableMonitoringType


class MonitoringDataType:
    def __init__(self, component: ComponentType, variable: VariableType, variableMonitoring: List[VariableMonitoringType]):
        self.component = component
        self.variable = variable
        self.variableMonitoring = variableMonitoring

    def to_dict(self):
        request = {
            "component" : self.component.to_dict(),
            "variable" : self.variable.to_dict(),
            "variableMonitoring" : [variableMonitoring.to_dict() for variableMonitoring in self.variableMonitoring],
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['component'] = ComponentType.sample(option=option)
        result['variable'] = VariableType.sample(option=option)
        result['variableMonitoring'] = [VariableMonitoringType.sample(option=option)]

        return result
    