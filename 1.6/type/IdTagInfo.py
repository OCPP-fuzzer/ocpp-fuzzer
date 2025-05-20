from datetime import datetime

from typing import Optional

from type.IdToken import IdToken
from type.AuthorizationStatus import AuthorizationStatus

class IdTagInfo:

    def __init__(self, status: AuthorizationStatus, expiryDate: Optional[datetime]= None, parentIdTag: Optional[IdToken]= None):
        self.status = status
        if expiryDate:
            self.expiryDate = expiryDate
        if parentIdTag:
            self.parentIdTag = parentIdTag

    def get_value(self):
        result = {
            "status" : self.status.get_value(),
        }
        if self.expiryDate:
            result['expiryDate'] = self.expiryDate.isoformat().split('.')[0] + 'Z'
        if self.parentIdTag:
            result['parentIdTag'] = self.parentIdTag.get_value()
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['status'] = AuthorizationStatus.get_sample(option=option)
        if option:
            result['expiryDate'] = datetime.now().isoformat().split('.')[0] + 'Z'
        if option:
            result['parentIdTag'] = IdToken.get_sample(option=option)
        return result