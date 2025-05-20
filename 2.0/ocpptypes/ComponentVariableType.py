from typing import Optional

from ocpptypes.ComponentType import ComponentType
from ocpptypes.VariableType import VariableType


class ComponentVariableType:
    def __init__(self, component: ComponentType, variable: Optional[VariableType] = None):
        self.component = component

        if variable:
            self.variable = variable

    def to_dict(self):
        request = {
            "component" : self.component.to_dict(),
        }

        if self.variable:
            request["variable"] = self.variable.to_dict()

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['component'] = ComponentType.sample(option=option)

        if option:
            result['variable'] = VariableType.sample(option=option)

        return result
    