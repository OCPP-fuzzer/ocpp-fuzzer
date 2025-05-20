
class GetLocalListVersionResponse:

    def __init__(self, listVersion: int):
        self.listVersion = listVersion

    def get_value(self):
        result = {
            "listVersion" : self.listVersion,
        }
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['listVersion'] = 1
        return result