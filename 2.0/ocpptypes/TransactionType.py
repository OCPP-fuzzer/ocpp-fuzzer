from typing import Optional

from ocppenum.ChargingStateEnumType import ChargingStateEnumType
from ocppenum.ReasonEnumType import ReasonEnumType

identifierString = str

class TransactionType:
    def __init__(self, transactionId: identifierString, chargingState: Optional[ChargingStateEnumType] = None, timeSpentCharging: Optional[int] = None, stoppedReason: Optional[ReasonEnumType] = None, remoteStartId: Optional[int] = None):
        self.transactionId = transactionId

        if chargingState:
            self.chargingState = chargingState
        if timeSpentCharging:
            self.timeSpentCharging = timeSpentCharging
        if stoppedReason:
            self.stoppedReason = stoppedReason
        if remoteStartId:
            self.remoteStartId = remoteStartId

    def to_dict(self):
        request = {
            "transactionId" : self.transactionId,
        }

        if self.chargingState:
            request["chargingState"] = self.chargingState.value
        if self.timeSpentCharging:
            request["timeSpentCharging"] = self.timeSpentCharging
        if self.stoppedReason:
            request["stoppedReason"] = self.stoppedReason.value
        if self.remoteStartId:
            request["remoteStartId"] = self.remoteStartId

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['transactionId'] = str(__import__('uuid').uuid4())

        if option:
            result['chargingState'] = ChargingStateEnumType.sample()
            result['timeSpentCharging'] = 1
            result['stoppedReason'] = ReasonEnumType.sample()
            result['remoteStartId'] = 1

        return result
    