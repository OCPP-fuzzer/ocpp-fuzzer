from typing import Optional

from datetime import datetime


class SecurityEventNotificationRequest:
    def __init__(self, type: str, timestamp: datetime, techInfo: Optional[str] = None):
        self.type = type
        self.timestamp = timestamp

        if techInfo:
            self.techInfo = techInfo

    def to_dict(self):
        request = {
            "type" : self.type,
            "timestamp" : self.timestamp.isoformat().split('.')[0] + 'Z',
        }

        if self.techInfo:
            request["techInfo"] = self.techInfo

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['type'] = "string"
        result['timestamp'] = datetime.now().isoformat().split('.')[0] + 'Z'

        if option:
            result['techInfo'] = "string"

        return result
    