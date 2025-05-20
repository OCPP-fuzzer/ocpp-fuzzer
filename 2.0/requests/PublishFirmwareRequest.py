from typing import Optional

identifierString = str

class PublishFirmwareRequest:
    def __init__(self, location: str, checksum: identifierString, retries: Optional[int] = None, retryInterval: Optional[int] = None):
        self.location = location
        self.checksum = checksum

        if retries:
            self.retries = retries
        if retryInterval:
            self.retryInterval = retryInterval

    def to_dict(self):
        request = {
            "location" : self.location,
            "checksum" : self.checksum,
        }

        if self.retries:
            request["retries"] = self.retries
        if self.retryInterval:
            request["retryInterval"] = self.retryInterval

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['location'] = "string"
        result['checksum'] = str(__import__('uuid').uuid4())

        if option:
            result['retries'] = 1
            result['retryInterval'] = 1

        return result
    