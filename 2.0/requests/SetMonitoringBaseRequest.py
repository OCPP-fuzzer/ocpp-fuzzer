from ocppenum.MonitoringBaseEnumType import MonitoringBaseEnumType


class SetMonitoringBaseRequest:
    def __init__(self, monitoringBase: MonitoringBaseEnumType):
        self.monitoringBase = monitoringBase

    def to_dict(self):
        request = {
            "monitoringBase" : self.monitoringBase.value,
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['monitoringBase'] = MonitoringBaseEnumType.sample()

        return result
    