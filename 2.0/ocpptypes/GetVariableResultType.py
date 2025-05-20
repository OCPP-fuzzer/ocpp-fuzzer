from typing import Optional

from ocppenum.GetVariableStatusEnumType import GetVariableStatusEnumType
from ocppenum.AttributeEnumType import AttributeEnumType
from ocpptypes.ComponentType import ComponentType
from ocpptypes.VariableType import VariableType
from ocpptypes.StatusInfoType import StatusInfoType


class GetVariableResultType:
    def __init__(self, attributeStatus: GetVariableStatusEnumType, component: ComponentType, variable: VariableType, attributeType: Optional[AttributeEnumType] = None, attributeValue: Optional[str] = None, attributeStatusInfo: Optional[StatusInfoType] = None):
        self.attributeStatus = attributeStatus
        self.component = component
        self.variable = variable

        if attributeType:
            self.attributeType = attributeType
        if attributeValue:
            self.attributeValue = attributeValue
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
        if self.attributeValue:
            request["attributeValue"] = self.attributeValue
        if self.attributeStatusInfo:
            request["attributeStatusInfo"] = self.attributeStatusInfo.to_dict()

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['attributeStatus'] = GetVariableStatusEnumType.sample()
        result['component'] = ComponentType.sample(option=option)
        result['variable'] = VariableType.sample(option=option)

        if option:
            result['attributeType'] = AttributeEnumType.sample()
            result['attributeValue'] = "string"
            result['attributeStatusInfo'] = StatusInfoType.sample(option=option)

        return result
    