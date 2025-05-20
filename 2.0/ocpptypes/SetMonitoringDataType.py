from typing import Optional

from ocppenum.MonitorEnumType import MonitorEnumType
from ocpptypes.ComponentType import ComponentType
from ocpptypes.VariableType import VariableType


class SetMonitoringDataType:
    def __init__(self, value: float, type: MonitorEnumType, severity: int, component: ComponentType, variable: VariableType, id: Optional[int] = None, transaction: Optional[bool] = None):
        self.value = value
        self.type = type
        self.severity = severity
        self.component = component
        self.variable = variable

        if id:
            self.id = id
        if transaction:
            self.transaction = transaction

    def to_dict(self):
        request = {
            "value" : self.value,
            "type" : self.type.value,
            "severity" : self.severity,
            "component" : self.component.to_dict(),
            "variable" : self.variable.to_dict(),
        }

        if self.id:
            request["id"] = self.id
        if self.transaction:
            request["transaction"] = self.transaction

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['value'] = 1.0
        result['type'] = MonitorEnumType.sample()
        result['severity'] = 1
        result['component'] = ComponentType.sample(option=option)
        result['variable'] = VariableType.sample(option=option)

        if option:
            result['id'] = 1
            result['transaction'] = True

        return result
    