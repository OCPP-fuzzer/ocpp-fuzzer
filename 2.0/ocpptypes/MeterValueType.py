from typing import List

from datetime import datetime

from ocpptypes.SampledValueType import SampledValueType


class MeterValueType:
    def __init__(self, timestamp: datetime, sampledValue: List[SampledValueType]):
        self.timestamp = timestamp
        self.sampledValue = sampledValue

    def to_dict(self):
        request = {
            "timestamp" : self.timestamp.isoformat().split('.')[0] + 'Z',
            "sampledValue" : [sampledValue.to_dict() for sampledValue in self.sampledValue],
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['timestamp'] = datetime.now().isoformat().split('.')[0] + 'Z'
        result['sampledValue'] = [SampledValueType.sample(option=option)]

        return result
    