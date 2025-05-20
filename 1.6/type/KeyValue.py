from typing import Optional

from type.CiString50Type import CiString50Type
from type.CiString500Type import CiString500Type

class KeyValue:

    def __init__(self, key: CiString50Type, readonly: bool, value: Optional[CiString500Type]= None):
        self.key = key
        self.readonly = readonly
        if value:
            self.value = value

    def get_value(self):
        result = {
            "key" : self.key.get_value(),
            "readonly" : self.readonly,
        }
        if self.value:
            result['value'] = self.value.get_value()
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['key'] = CiString50Type.get_sample(option=option)
        result['readonly'] = __import__('random').choice([True, False])
        if option:
            result['value'] = CiString500Type.get_sample(option=option)
        return result