from typing import Optional

from ocppenum.SetMonitoringStatusEnumType import SetMonitoringStatusEnumType
from ocppenum.MonitorEnumType import MonitorEnumType
from ocpptypes.ComponentType import ComponentType
from ocpptypes.VariableType import VariableType
from ocpptypes.StatusInfoType import StatusInfoType


class SetMonitoringResultType:
    def __init__(self, status: SetMonitoringStatusEnumType, type: MonitorEnumType, severity: int, component: ComponentType, variable: VariableType, id: Optional[int] = None, statusInfo: Optional[StatusInfoType] = None):
        self.status = status
        self.type = type
        self.severity = severity
        self.component = component
        self.variable = variable

        if id:
            self.id = id
        if statusInfo:
            self.statusInfo = statusInfo

    def to_dict(self):
        request = {
            "status" : self.status.value,
            "type" : self.type.value,
            "severity" : self.severity,
            "component" : self.component.to_dict(),
            "variable" : self.variable.to_dict(),
        }

        if self.id:
            request["id"] = self.id
        if self.statusInfo:
            request["statusInfo"] = self.statusInfo.to_dict()

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['status'] = SetMonitoringStatusEnumType.sample()
        result['type'] = MonitorEnumType.sample()
        result['severity'] = 1
        result['component'] = ComponentType.sample(option=option)
        result['variable'] = VariableType.sample(option=option)

        if option:
            result['id'] = 1
            result['statusInfo'] = StatusInfoType.sample(option=option)

        return result
    