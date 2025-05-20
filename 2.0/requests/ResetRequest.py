from typing import Optional

from ocppenum.ResetEnumType import ResetEnumType


class ResetRequest:
    def __init__(self, type: ResetEnumType, evseId: Optional[int] = None):
        self.type = type

        if evseId:
            self.evseId = evseId

    def to_dict(self):
        request = {
            "type" : self.type.value,
        }

        if self.evseId:
            request["evseId"] = self.evseId

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['type'] = ResetEnumType.sample()

        if option:
            result['evseId'] = 1

        return result
    