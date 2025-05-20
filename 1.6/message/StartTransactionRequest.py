from datetime import datetime

from typing import Optional

from type.IdToken import IdToken

class StartTransactionRequest:

    def __init__(self, connectorId: int, idTag: IdToken, meterStart: int, timestamp: datetime, reservationId: Optional[int]= None):
        self.connectorId = connectorId
        self.idTag = idTag
        self.meterStart = meterStart
        self.timestamp = timestamp
        if reservationId:
            self.reservationId = reservationId

    def get_value(self):
        result = {
            "connectorId" : self.connectorId,
            "idTag" : self.idTag.get_value(),
            "meterStart" : self.meterStart,
            "timestamp" : self.timestamp.isoformat().split('.')[0] + 'Z',
        }
        if self.reservationId:
            result['reservationId'] = self.reservationId
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['connectorId'] = 1
        result['idTag'] = IdToken.get_sample(option=option)
        result['meterStart'] = 1
        result['timestamp'] = datetime.now().isoformat().split('.')[0] + 'Z'
        if option:
            result['reservationId'] = 1
        return result