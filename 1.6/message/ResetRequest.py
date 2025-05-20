from type.ResetType import ResetType

class ResetRequest:

    def __init__(self, type: ResetType):
        self.type = type

    def get_value(self):
        result = {
            "type" : self.type.get_value(),
        }
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['type'] = ResetType.get_sample(option=option)
        return result