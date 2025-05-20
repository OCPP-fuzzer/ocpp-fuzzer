from typing import List, Optional

from ocppenum.UpdateEnumType import UpdateEnumType
from ocpptypes.AuthorizationData import AuthorizationData


class SendLocalListRequest:
    def __init__(self, versionNumber: int, updateType: UpdateEnumType, localAuthorizationList: Optional[List[AuthorizationData]] = None):
        self.versionNumber = versionNumber
        self.updateType = updateType

        if localAuthorizationList:
            self.localAuthorizationList = localAuthorizationList

    def to_dict(self):
        request = {
            "versionNumber" : self.versionNumber,
            "updateType" : self.updateType.value,
        }

        if self.localAuthorizationList:
            request["localAuthorizationList"] = [localAuthorizationList.to_dict() for localAuthorizationList in self.localAuthorizationList]

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['versionNumber'] = 1
        result['updateType'] = UpdateEnumType.sample()

        if option:
            result['localAuthorizationList'] = [AuthorizationData.sample(option=option)]

        return result
    