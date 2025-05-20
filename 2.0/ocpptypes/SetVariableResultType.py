from typing import Optional

from ocppenum.AttributeEnumType import AttributeEnumType
from ocppenum.SetVariableStatusEnumType import SetVariableStatusEnumType
from ocpptypes.ComponentType import ComponentType
from ocpptypes.VariableType import VariableType
from ocpptypes.StatusInfoType import StatusInfoType


class SetVariableResultType:
    def __init__(self, attributeStatus: SetVariableStatusEnumType, component: ComponentType, variable: VariableType, attributeType: Optional[AttributeEnumType] = None, attributeStatusInfo: Optional[StatusInfoType] = None):
        self.attributeStatus = attributeStatus
        self.component = component
        self.variable = variable

        if attributeType:
            self.attributeType = attributeType
        if attributeStatusInfo:
            self.attributeStatusInfo = attributeStatusInfo

    def to_dict(self):
        request = {
            "attributeStatus" : self.attributeStatus.value,
            "component" : self.component.to_dict(),
            "variable" : self.variable.to_dict(),
        }

        if self.attributeType:
            request["attributeType"] = self.attributeType.value
        if self.attributeStatusInfo:
            request["attributeStatusInfo"] = self.attributeStatusInfo.to_dict()

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['attributeStatus'] = SetVariableStatusEnumType.sample()
        result['component'] = ComponentType.sample(option=option)
        result['variable'] = VariableType.sample(option=option)

        if option:
            result['attributeType'] = AttributeEnumType.sample()
            result['attributeStatusInfo'] = StatusInfoType.sample(option=option)

        return result
    