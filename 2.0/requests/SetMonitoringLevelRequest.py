
class SetMonitoringLevelRequest:
    def __init__(self, severity: int):
        self.severity = severity

    def to_dict(self):
        request = {
            "severity" : self.severity,
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['severity'] = 1

        return result
    