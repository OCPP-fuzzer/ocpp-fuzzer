from datetime import datetime

from typing import Optional

from type.IdToken import IdToken

class ReserveNowRequest:

    def __init__(self, connectorId: int, expiryDate: datetime, idTag: IdToken, reservationId: int, parentIdTag: Optional[IdToken]= None):
        self.connectorId = connectorId
        self.expiryDate = expiryDate
        self.idTag = idTag
        self.reservationId = reservationId
        if parentIdTag:
            self.parentIdTag = parentIdTag

    def get_value(self):
        result = {
            "connectorId" : self.connectorId,
            "expiryDate" : self.expiryDate.isoformat().split('.')[0] + 'Z',
            "idTag" : self.idTag.get_value(),
            "reservationId" : self.reservationId,
        }
        if self.parentIdTag:
            result['parentIdTag'] = self.parentIdTag.get_value()
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['connectorId'] = 1
        result['expiryDate'] = datetime.now().isoformat().split('.')[0] + 'Z'
        result['idTag'] = IdToken.get_sample(option=option)
        result['reservationId'] = 1
        if option:
            result['parentIdTag'] = IdToken.get_sample(option=option)
        return result