from type.FirmwareStatus import FirmwareStatus

class FirmwareStatusNotificationRequest:

    def __init__(self, status: FirmwareStatus):
        self.status = status

    def get_value(self):
        result = {
            "status" : self.status.get_value(),
        }
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['status'] = FirmwareStatus.get_sample(option=option)
        return result