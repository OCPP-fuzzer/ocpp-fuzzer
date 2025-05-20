from typing import List, Optional

from type.MeterValue import MeterValue

class MeterValuesRequest:

    def __init__(self, connectorId: int, meterValue: List[MeterValue], transactionId: Optional[int]= None):
        self.connectorId = connectorId
        self.meterValue = meterValue
        if transactionId:
            self.transactionId = transactionId

    def get_value(self):
        result = {
            "connectorId" : self.connectorId,
            "meterValue" : [ meterValue.get_value() for meterValue in self.meterValue ],
        }
        if self.transactionId:
            result['transactionId'] = self.transactionId
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['connectorId'] = 1
        result['meterValue'] = [ MeterValue.get_sample(option=option), ]
        if option:
            result['transactionId'] = 1
        return result