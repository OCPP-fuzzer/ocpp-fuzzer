from type.RemoteStartStopStatus import RemoteStartStopStatus

class RemoteStartTransactionResponse:

    def __init__(self, status: RemoteStartStopStatus):
        self.status = status

    def get_value(self):
        result = {
            "status" : self.status.get_value(),
        }
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['status'] = RemoteStartStopStatus.get_sample(option=option)
        return result