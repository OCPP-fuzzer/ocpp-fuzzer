from datetime import datetime

class HeartbeatResponse:

    def __init__(self, currentTime: datetime):
        self.currentTime = currentTime

    def get_value(self):
        result = {
            "currentTime" : self.currentTime.isoformat().split('.')[0] + 'Z',
        }
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['currentTime'] = datetime.now().isoformat().split('.')[0] + 'Z'
        return result