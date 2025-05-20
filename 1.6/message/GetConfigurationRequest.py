from typing import List, Optional

from type.CiString50Type import CiString50Type

class GetConfigurationRequest:

    def __init__(self, key: Optional[List[CiString50Type]]= None):
        if key:
            self.key = key

    def get_value(self):
        result = {
        }
        if self.key:
            result['key'] = [ key.get_value() for key in self.key ]
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        if option:
            result['key'] = [ CiString50Type.get_sample(option=option), ]
        return result