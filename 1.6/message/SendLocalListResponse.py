from type.UpdateStatus import UpdateStatus

class SendLocalListResponse:

    def __init__(self, status: UpdateStatus):
        self.status = status

    def get_value(self):
        result = {
            "status" : self.status.get_value(),
        }
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['status'] = UpdateStatus.get_sample(option=option)
        return result