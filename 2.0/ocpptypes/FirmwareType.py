from typing import Optional

from datetime import datetime


class FirmwareType:
    def __init__(self, location: str, retrieveDateTime: datetime, installDateTime: Optional[datetime] = None, signingCertificate: Optional[str] = None, signature: Optional[str] = None):
        self.location = location
        self.retrieveDateTime = retrieveDateTime

        if installDateTime:
            self.installDateTime = installDateTime
        if signingCertificate:
            self.signingCertificate = signingCertificate
        if signature:
            self.signature = signature

    def to_dict(self):
        request = {
            "location" : self.location,
            "retrieveDateTime" : self.retrieveDateTime.isoformat().split('.')[0] + 'Z',
        }

        if self.installDateTime:
            request["installDateTime"] = self.installDateTime.isoformat().split('.')[0] + 'Z'
        if self.signingCertificate:
            request["signingCertificate"] = self.signingCertificate
        if self.signature:
            request["signature"] = self.signature

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['location'] = "string"
        result['retrieveDateTime'] = datetime.now().isoformat().split('.')[0] + 'Z'

        if option:
            result['installDateTime'] = datetime.now().isoformat().split('.')[0] + 'Z'
            result['signingCertificate'] = "string"
            result['signature'] = "string"

        return result
    