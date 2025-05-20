from typing import List, Optional

from type.AuthorizationData import AuthorizationData
from type.UpdateType import UpdateType

class SendLocalListRequest:

    def __init__(self, listVersion: int, updateType: UpdateType, localAuthorizationList: Optional[List[AuthorizationData]]= None):
        self.listVersion = listVersion
        self.updateType = updateType
        if localAuthorizationList:
            self.localAuthorizationList = localAuthorizationList

    def get_value(self):
        result = {
            "listVersion" : self.listVersion,
            "updateType" : self.updateType.get_value(),
        }
        if self.localAuthorizationList:
            result['localAuthorizationList'] = [ localAuthorizationList.get_value() for localAuthorizationList in self.localAuthorizationList ]
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['listVersion'] = 1
        result['updateType'] = UpdateType.get_sample(option=option)
        if option:
            result['localAuthorizationList'] = [ AuthorizationData.get_sample(option=option), ]
        return result