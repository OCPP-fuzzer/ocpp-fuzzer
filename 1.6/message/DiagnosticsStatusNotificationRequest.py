from type.DiagnosticsStatus import DiagnosticsStatus

class DiagnosticsStatusNotificationRequest:

    def __init__(self, status: DiagnosticsStatus):
        self.status = status

    def get_value(self):
        result = {
            "status" : self.status.get_value(),
        }
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['status'] = DiagnosticsStatus.get_sample(option=option)
        return result