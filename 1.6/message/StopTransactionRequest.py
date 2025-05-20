from datetime import datetime

from typing import List, Optional

from type.Reason import Reason
from type.IdToken import IdToken
from type.MeterValue import MeterValue

class StopTransactionRequest:

    def __init__(self,
        meterStop: int,
        timestamp: datetime,
        transactionId: int,
        idTag: Optional[IdToken]= None,
        reason: Optional[Reason]= None,
        transactionData: Optional[List[MeterValue]]= None
    ):
        self.meterStop = meterStop
        self.timestamp = timestamp
        self.transactionId = transactionId
        if idTag:
            self.idTag = idTag
        if reason:
            self.reason = reason
        if transactionData:
            self.transactionData = transactionData

    def get_value(self):
        result = {
            "meterStop" : self.meterStop,
            "timestamp" : self.timestamp.isoformat().split('.')[0] + 'Z',
            "transactionId" : self.transactionId,
        }
        if self.idTag:
            result['idTag'] = self.idTag.get_value()
        if self.reason:
            result['reason'] = self.reason.get_value()
        if self.transactionData:
            result['transactionData'] = [ transactionData.get_value() for transactionData in self.transactionData ]
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['meterStop'] = 1
        result['timestamp'] = datetime.now().isoformat().split('.')[0] + 'Z'
        result['transactionId'] = 1
        if option:
            result['idTag'] = IdToken.get_sample(option=option)
        if option:
            result['reason'] = Reason.get_sample(option=option)
        if option:
            result['transactionData'] = [ MeterValue.get_sample(option=option), ]
        return result