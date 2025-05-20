from typing import Optional

from datetime import datetime

from ocppenum.ConnectorEnumType import ConnectorEnumType
from ocpptypes.IdTokenType import IdTokenType
from ocpptypes.IdTokenType import IdTokenType


class ReserveNowRequest:
    def __init__(self, id: int, expiryDateTime: datetime, idToken: IdTokenType, connectorType: Optional[ConnectorEnumType] = None, evseld: Optional[int] = None, groupIdToken: Optional[IdTokenType] = None):
        self.id = id
        self.expiryDateTime = expiryDateTime
        self.idToken = idToken

        if connectorType:
            self.connectorType = connectorType
        if evseld:
            self.evseld = evseld
        if groupIdToken:
            self.groupIdToken = groupIdToken

    def to_dict(self):
        request = {
            "id" : self.id,
            "expiryDateTime" : self.expiryDateTime.isoformat().split('.')[0] + 'Z',
            "idToken" : self.idToken.to_dict(),
        }

        if self.connectorType:
            request["connectorType"] = self.connectorType.value
        if self.evseld:
            request["evseld"] = self.evseld
        if self.groupIdToken:
            request["groupIdToken"] = self.groupIdToken.to_dict()

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['id'] = 1
        result['expiryDateTime'] = datetime.now().isoformat().split('.')[0] + 'Z'
        result['idToken'] = IdTokenType.sample(option=option)

        if option:
            result['connectorType'] = ConnectorEnumType.sample()
            result['evseld'] = 1
            result['groupIdToken'] = IdTokenType.sample(option=option)

        return result
    