from typing import List

from ocpptypes.MeterValueType import MeterValueType


class MeterValuesRequest:
    def __init__(self, evseId: int, meterValue: List[MeterValueType]):
        self.evseId = evseId
        self.meterValue = meterValue

    def to_dict(self):
        request = {
            "evseId" : self.evseId,
            "meterValue" : [meterValue.to_dict() for meterValue in self.meterValue],
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['evseId'] = 1
        result['meterValue'] = [MeterValueType.sample(option=option)]

        return result
    