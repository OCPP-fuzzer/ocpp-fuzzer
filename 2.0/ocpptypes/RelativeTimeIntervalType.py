from typing import Optional


class RelativeTimeIntervalType:
    def __init__(self, start: int, duration: Optional[int] = None):
        self.start = start

        if duration:
            self.duration = duration

    def to_dict(self):
        request = {
            "start" : self.start,
        }

        if self.duration:
            request["duration"] = self.duration

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['start'] = 1

        if option:
            result['duration'] = 1

        return result
    