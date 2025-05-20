from datetime import datetime

from typing import Optional

class GetDiagnosticsRequest:

    def __init__(self, location: str, retries: Optional[int]= None, retryInterval: Optional[int]= None, startTime: Optional[datetime]= None, stopTime: Optional[datetime]= None):
        self.location = location
        if retries:
            self.retries = retries
        if retryInterval:
            self.retryInterval = retryInterval
        if startTime:
            self.startTime = startTime
        if stopTime:
            self.stopTime = stopTime

    def get_value(self):
        result = {
            "location" : self.location,
        }
        if self.retries:
            result['retries'] = self.retries
        if self.retryInterval:
            result['retryInterval'] = self.retryInterval
        if self.startTime:
            result['startTime'] = self.startTime.isoformat().split('.')[0] + 'Z'
        if self.stopTime:
            result['stopTime'] = self.stopTime.isoformat().split('.')[0] + 'Z'
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['location'] = "http://example.com/"
        if option:
            result['retries'] = 1
        if option:
            result['retryInterval'] = 1
        if option:
            result['startTime'] = datetime.now().isoformat().split('.')[0] + 'Z'
        if option:
            result['stopTime'] = datetime.now().isoformat().split('.')[0] + 'Z'
        return result