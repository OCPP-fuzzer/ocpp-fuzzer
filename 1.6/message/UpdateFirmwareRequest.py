from datetime import datetime

from typing import Optional

class UpdateFirmwareRequest:

    def __init__(self, location: str, retrieveDate: datetime, retries: Optional[int]= None, retryInterval: Optional[int]= None):
        self.location = location
        self.retrieveDate = retrieveDate
        if retries:
            self.retries = retries
        if retryInterval:
            self.retryInterval = retryInterval

    def get_value(self):
        result = {
            "location" : self.location,
            "retrieveDate" : self.retrieveDate.isoformat().split('.')[0] + 'Z',
        }
        if self.retries:
            result['retries'] = self.retries
        if self.retryInterval:
            result['retryInterval'] = self.retryInterval
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['location'] = "http://example.com/"
        result['retrieveDate'] = datetime.now().isoformat().split('.')[0] + 'Z'
        if option:
            result['retries'] = 1
        if option:
            result['retryInterval'] = 1
        return result