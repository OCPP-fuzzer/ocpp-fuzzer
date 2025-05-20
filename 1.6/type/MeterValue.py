from datetime import datetime

from typing import List

from type.SampledValue import SampledValue

class MeterValue:

    def __init__(self, timestamp: datetime, sampledValue: List[SampledValue]):
        self.timestamp = timestamp
        self.sampledValue = sampledValue

    def get_value(self):
        result = {
            "timestamp" : self.timestamp.isoformat().split('.')[0] + 'Z',
            "sampledValue" : [ sampledValue.get_value() for sampledValue in self.sampledValue ],
        }
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['timestamp'] = datetime.now().isoformat().split('.')[0] + 'Z'
        result['sampledValue'] = [ SampledValue.get_sample(option=option), ]
        return result