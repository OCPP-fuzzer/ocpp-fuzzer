from typing import List, Optional

from type.CiString50Type import CiString50Type
from type.KeyValue import KeyValue

class GetConfigurationResponse:

    def __init__(self, configurationKey: Optional[List[KeyValue]]= None, unknownKey: Optional[List[CiString50Type]]= None):
        if configurationKey:
            self.configurationKey = configurationKey
        if unknownKey:
            self.unknownKey = unknownKey

    def get_value(self):
        result = {
        }
        if self.configurationKey:
            result['configurationKey'] = [ configurationKey.get_value() for configurationKey in self.configurationKey ]
        if self.unknownKey:
            result['unknownKey'] = [ unknownKey.get_value() for unknownKey in self.unknownKey ]
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        if option:
            result['configurationKey'] = [ KeyValue.get_sample(option=option), ]
        if option:
            result['unknownKey'] = [ CiString50Type.get_sample(option=option), ]
        return result