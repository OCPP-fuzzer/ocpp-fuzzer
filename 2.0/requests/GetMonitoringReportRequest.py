from typing import List, Optional

from ocppenum.MonitoringCriterionEnumType import MonitoringCriterionEnumType
from ocpptypes.ComponentVariableType import ComponentVariableType


class GetMonitoringReportRequest:
    def __init__(self, requestId: int, monitoringCriteria: Optional[List[MonitoringCriterionEnumType]] = None, componentVariable: Optional[List[ComponentVariableType]] = None):
        self.requestId = requestId

        if monitoringCriteria:
            self.monitoringCriteria = monitoringCriteria
        if componentVariable:
            self.componentVariable = componentVariable

    def to_dict(self):
        request = {
            "requestId" : self.requestId,
        }

        if self.monitoringCriteria:
            request["monitoringCriteria"] = [monitoringCriteria.value for monitoringCriteria in self.monitoringCriteria]
        if self.componentVariable:
            request["componentVariable"] = [componentVariable.to_dict() for componentVariable in self.componentVariable]

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['requestId'] = 1

        if option:
            result['monitoringCriteria'] = [MonitoringCriterionEnumType.sample()]
            result['componentVariable'] = [ComponentVariableType.sample(option=option)]

        return result
    