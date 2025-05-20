from typing import Optional, List

from ocpptypes.ComponentType import ComponentType
from ocpptypes.VariableType import VariableType
from ocpptypes.VariableAttributeType import VariableAttributeType
from ocpptypes.VariableCharacteristicsType import VariableCharacteristicsType


class ReportDataType:
    def __init__(self, component: ComponentType, variable: VariableType, variableAttribute: List[VariableAttributeType], variableCharacteristics: Optional[VariableCharacteristicsType] = None):
        self.component = component
        self.variable = variable
        self.variableAttribute = variableAttribute

        if variableCharacteristics:
            self.variableCharacteristics = variableCharacteristics

    def to_dict(self):
        request = {
            "component" : self.component.to_dict(),
            "variable" : self.variable.to_dict(),
            "variableAttribute" : [variableAttribute.to_dict() for variableAttribute in self.variableAttribute],
        }

        if self.variableCharacteristics:
            request["variableCharacteristics"] = self.variableCharacteristics.to_dict()

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['component'] = ComponentType.sample(option=option)
        result['variable'] = VariableType.sample(option=option)
        result['variableAttribute'] = [VariableAttributeType.sample(option=option)]

        if option:
            result['variableCharacteristics'] = VariableCharacteristicsType.sample(option=option)

        return result
    