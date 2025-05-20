from typing import Optional

from ocppenum.AttributeEnumType import AttributeEnumType
from ocpptypes.ComponentType import ComponentType
from ocpptypes.VariableType import VariableType


class GetVariableDataType:
    def __init__(self, component: ComponentType, variable: VariableType, attributeType: Optional[AttributeEnumType] = None):
        self.component = component
        self.variable = variable

        if attributeType:
            self.attributeType = attributeType

    def to_dict(self):
        request = {
            "component" : self.component.to_dict(),
            "variable" : self.variable.to_dict(),
        }

        if self.attributeType:
            request["attributeType"] = self.attributeType.value

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['component'] = ComponentType.sample(option=option)
        result['variable'] = VariableType.sample(option=option)

        if option:
            result['attributeType'] = AttributeEnumType.sample()

        return result
    