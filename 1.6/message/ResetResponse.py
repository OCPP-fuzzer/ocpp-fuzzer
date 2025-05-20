from type.ResetStatus import ResetStatus

class ResetResponse:

    def __init__(self, status: ResetStatus):
        self.status = status

    def get_value(self):
        result = {
            "status" : self.status.get_value(),
        }
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['status'] = ResetStatus.get_sample(option=option)
        return result