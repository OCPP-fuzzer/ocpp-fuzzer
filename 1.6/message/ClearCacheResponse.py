from type.ClearCacheStatus import ClearCacheStatus

class ClearCacheResponse:

    def __init__(self, status: ClearCacheStatus):
        self.status = status

    def get_value(self):
        result = {
            "status" : self.status.get_value(),
        }
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['status'] = ClearCacheStatus.get_sample(option=option)
        return result