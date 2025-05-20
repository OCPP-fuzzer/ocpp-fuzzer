from type.UnlockStatus import UnlockStatus

class UnlockConnectorResponse:

    def __init__(self, status: UnlockStatus):
        self.status = status

    def get_value(self):
        result = {
            "status" : self.status.get_value(),
        }
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['status'] = UnlockStatus.get_sample(option=option)
        return result