from typing import List, Optional

from ocppenum.ComponentCriterionEnumType import ComponentCriterionEnumType
from ocpptypes.ComponentVariableType import ComponentVariableType


class GetReportRequest:
    def __init__(self, requestId: int, componentCriteria: Optional[List[ComponentCriterionEnumType]] = None, componentVariable: Optional[List[ComponentVariableType]] = None):
        self.requestId = requestId

        if componentCriteria:
            self.componentCriteria = componentCriteria
        if componentVariable:
            self.componentVariable = componentVariable

    def to_dict(self):
        request = {
            "requestId" : self.requestId,
        }

        if self.componentCriteria:
            request["componentCriteria"] = [componentCriteria.value for componentCriteria in self.componentCriteria]
        if self.componentVariable:
            request["componentVariable"] = [componentVariable.to_dict() for componentVariable in self.componentVariable]

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['requestId'] = 1

        if option:
            result['componentCriteria'] = [ComponentCriterionEnumType.sample()]
            result['componentVariable'] = [ComponentVariableType.sample(option=option)]

        return result
    