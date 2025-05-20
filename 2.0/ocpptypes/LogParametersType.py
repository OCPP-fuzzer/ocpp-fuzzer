from typing import Optional

from datetime import datetime


class LogParametersType:
    def __init__(self, remoteLocation: str, oldestTimestamp: Optional[datetime] = None, latestTimestamp: Optional[datetime] = None):
        self.remoteLocation = remoteLocation

        if oldestTimestamp:
            self.oldestTimestamp = oldestTimestamp
        if latestTimestamp:
            self.latestTimestamp = latestTimestamp

    def to_dict(self):
        request = {
            "remoteLocation" : self.remoteLocation,
        }

        if self.oldestTimestamp:
            request["oldestTimestamp"] = self.oldestTimestamp.isoformat().split('.')[0] + 'Z'
        if self.latestTimestamp:
            request["latestTimestamp"] = self.latestTimestamp.isoformat().split('.')[0] + 'Z'

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['remoteLocation'] = "string"

        if option:
            result['oldestTimestamp'] = datetime.now().isoformat().split('.')[0] + 'Z'
            result['latestTimestamp'] = datetime.now().isoformat().split('.')[0] + 'Z'

        return result
    