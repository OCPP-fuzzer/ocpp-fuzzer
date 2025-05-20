from ocppenum.MonitorEnumType import MonitorEnumType


class VariableMonitoringType:
    def __init__(self, id: int, transaction: bool, value: float, type: MonitorEnumType, severity: int):
        self.id = id
        self.transaction = transaction
        self.value = value
        self.type = type
        self.severity = severity

    def to_dict(self):
        request = {
            "id" : self.id,
            "transaction" : self.transaction,
            "value" : self.value,
            "type" : self.type.value,
            "severity" : self.severity,
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['id'] = 1
        result['transaction'] = True
        result['value'] = 1.0
        result['type'] = MonitorEnumType.sample()
        result['severity'] = 1

        return result
    