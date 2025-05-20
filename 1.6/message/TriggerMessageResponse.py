from type.TriggerMessageStatus import TriggerMessageStatus

class TriggerMessageResponse:

    def __init__(self, status: TriggerMessageStatus):
        self.status = status

    def get_value(self):
        result = {
            "status" : self.status.get_value(),
        }
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['status'] = TriggerMessageStatus.get_sample(option=option)
        return result