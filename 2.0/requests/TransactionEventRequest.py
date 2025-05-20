from typing import List, Optional

from datetime import datetime

from ocppenum.TransactionEventEnumType import TransactionEventEnumType
from ocppenum.TriggerReasonEnumType import TriggerReasonEnumType
from ocpptypes.TransactionType import TransactionType
from ocpptypes.IdTokenType import IdTokenType
from ocpptypes.EVSEType import EVSEType
from ocpptypes.MeterValueType import MeterValueType


class TransactionEventRequest:
    def __init__(self, eventType: TransactionEventEnumType, timestamp: datetime, triggerReason: TriggerReasonEnumType, seqNo: int, transactionInfo: TransactionType, offline: Optional[bool] = None, numberOfPhasesUsed: Optional[int] = None, cableMaxCurrent: Optional[int] = None, reservationId: Optional[int] = None, idToken: Optional[IdTokenType] = None, evse: Optional[EVSEType] = None, meterValue: Optional[List[MeterValueType]] = None):
        self.eventType = eventType
        self.timestamp = timestamp
        self.triggerReason = triggerReason
        self.seqNo = seqNo
        self.transactionInfo = transactionInfo

        if offline:
            self.offline = offline
        if numberOfPhasesUsed:
            self.numberOfPhasesUsed = numberOfPhasesUsed
        if cableMaxCurrent:
            self.cableMaxCurrent = cableMaxCurrent
        if reservationId:
            self.reservationId = reservationId
        if idToken:
            self.idToken = idToken
        if evse:
            self.evse = evse
        if meterValue:
            self.meterValue = meterValue

    def to_dict(self):
        request = {
            "eventType" : self.eventType.value,
            "timestamp" : self.timestamp.isoformat().split('.')[0] + 'Z',
            "triggerReason" : self.triggerReason.value,
            "seqNo" : self.seqNo,
            "transactionInfo" : self.transactionInfo.to_dict(),
        }

        if self.offline:
            request["offline"] = self.offline
        if self.numberOfPhasesUsed:
            request["numberOfPhasesUsed"] = self.numberOfPhasesUsed
        if self.cableMaxCurrent:
            request["cableMaxCurrent"] = self.cableMaxCurrent
        if self.reservationId:
            request["reservationId"] = self.reservationId
        if self.idToken:
            request["idToken"] = self.idToken.to_dict()
        if self.evse:
            request["evse"] = self.evse.to_dict()
        if self.meterValue:
            request["meterValue"] = [meterValue.to_dict() for meterValue in self.meterValue]

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['eventType'] = TransactionEventEnumType.sample()
        result['timestamp'] = datetime.now().isoformat().split('.')[0] + 'Z'
        result['triggerReason'] = TriggerReasonEnumType.sample()
        result['seqNo'] = 1
        result['transactionInfo'] = TransactionType.sample(option=option)

        if option:
            result['offline'] = True
            result['numberOfPhasesUsed'] = 1
            result['cableMaxCurrent'] = 1
            result['reservationId'] = 1
            result['idToken'] = IdTokenType.sample(option=option)
            result['evse'] = EVSEType.sample(option=option)
            result['meterValue'] = [MeterValueType.sample(option=option)]

        return result
    