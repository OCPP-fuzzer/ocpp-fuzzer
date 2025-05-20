from datetime import datetime

from type.RegistrationStatus import RegistrationStatus

class BootNotificationResponse:

    def __init__(self, currentTime: datetime, interval: int, status: RegistrationStatus):
        self.currentTime = currentTime
        self.interval = interval
        self.status = status

    def get_value(self):
        result = {
            "currentTime" : self.currentTime.isoformat().split('.')[0] + 'Z',
            "interval" : self.interval,
            "status" : self.status.get_value(),
        }
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['currentTime'] = datetime.now().isoformat().split('.')[0] + 'Z'
        result['interval'] = 1
        result['status'] = RegistrationStatus.get_sample(option=option)
        return result