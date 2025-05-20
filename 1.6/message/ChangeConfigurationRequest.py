from type.CiString50Type import CiString50Type
from type.CiString500Type import CiString500Type

class ChangeConfigurationRequest:

    def __init__(self, key: CiString50Type, value: CiString500Type):
        self.key = key
        self.value = value

    def get_value(self):
        result = {
            "key" : self.key.get_value(),
            "value" : self.value.get_value(),
        }
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['key'] = CiString50Type.get_sample(option=option)
        result['value'] = CiString500Type.get_sample(option=option)
        return result