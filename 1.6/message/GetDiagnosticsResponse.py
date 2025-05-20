from typing import Optional

from type.CiString255Type import CiString255Type

class GetDiagnosticsResponse:

    def __init__(self, fileName: Optional[CiString255Type]= None):
        if fileName:
            self.fileName = fileName

    def get_value(self):
        result = {
        }
        if self.fileName:
            result['fileName'] = self.fileName.get_value()
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        if option:
            result['fileName'] = CiString255Type.get_sample(option=option)
        return result