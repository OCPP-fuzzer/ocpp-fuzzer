from typing import Optional

from ocppenum.DataEnumType import DataEnumType


class VariableCharacteristicsType:
    def __init__(self, dataType: DataEnumType, supportsMonitoring: bool, unit: Optional[str] = None, minLimit: Optional[float] = None, maxLimit: Optional[float] = None, valuesList: Optional[str] = None):
        self.dataType = dataType
        self.supportsMonitoring = supportsMonitoring

        if unit:
            self.unit = unit
        if minLimit:
            self.minLimit = minLimit
        if maxLimit:
            self.maxLimit = maxLimit
        if valuesList:
            self.valuesList = valuesList

    def to_dict(self):
        request = {
            "dataType" : self.dataType.value,
            "supportsMonitoring" : self.supportsMonitoring,
        }

        if self.unit:
            request["unit"] = self.unit
        if self.minLimit:
            request["minLimit"] = self.minLimit
        if self.maxLimit:
            request["maxLimit"] = self.maxLimit
        if self.valuesList:
            request["valuesList"] = self.valuesList

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['dataType'] = DataEnumType.sample()
        result['supportsMonitoring'] = True

        if option:
            result['unit'] = "string"
            result['minLimit'] = 1.0
            result['maxLimit'] = 1.0
            result['valuesList'] = "string"

        return result
    