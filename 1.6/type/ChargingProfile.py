from datetime import datetime

from typing import Optional

from type.ChargingProfileKindType import ChargingProfileKindType
from type.RecurrencyKindType import RecurrencyKindType
from type.ChargingProfilePurposeType import ChargingProfilePurposeType
from type.ChargingSchedule import ChargingSchedule

class ChargingProfile:

    def __init__(self,
        chargingProfileId: int,
        stackLevel: int,
        chargingProfilePurpose: ChargingProfilePurposeType,
        chargingProfileKind: ChargingProfileKindType,
        chargingSchedule: ChargingSchedule,
        transactionId: Optional[int]= None,
        recurrencyKind: Optional[RecurrencyKindType]= None,
        validFrom: Optional[datetime]= None,
        validTo: Optional[datetime]= None
    ):
        self.chargingProfileId = chargingProfileId
        self.stackLevel = stackLevel
        self.chargingProfilePurpose = chargingProfilePurpose
        self.chargingProfileKind = chargingProfileKind
        self.chargingSchedule = chargingSchedule
        if transactionId:
            self.transactionId = transactionId
        if recurrencyKind:
            self.recurrencyKind = recurrencyKind
        if validFrom:
            self.validFrom = validFrom
        if validTo:
            self.validTo = validTo

    def get_value(self):
        result = {
            "chargingProfileId" : self.chargingProfileId,
            "stackLevel" : self.stackLevel,
            "chargingProfilePurpose" : self.chargingProfilePurpose.get_value(),
            "chargingProfileKind" : self.chargingProfileKind.get_value(),
            "chargingSchedule" : self.chargingSchedule.get_value(),
        }
        if self.transactionId:
            result['transactionId'] = self.transactionId
        if self.recurrencyKind:
            result['recurrencyKind'] = self.recurrencyKind.get_value()
        if self.validFrom:
            result['validFrom'] = self.validFrom.isoformat().split('.')[0] + 'Z'
        if self.validTo:
            result['validTo'] = self.validTo.isoformat().split('.')[0] + 'Z'
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['chargingProfileId'] = 1
        result['stackLevel'] = 1
        result['chargingProfilePurpose'] = ChargingProfilePurposeType.get_sample(option=option)
        result['chargingProfileKind'] = ChargingProfileKindType.get_sample(option=option)
        result['chargingSchedule'] = ChargingSchedule.get_sample(option=option)
        if option:
            result['transactionId'] = 1
        if option:
            result['recurrencyKind'] = RecurrencyKindType.get_sample(option=option)
        if option:
            result['validFrom'] = datetime.now().isoformat().split('.')[0] + 'Z'
        if option:
            result['validTo'] = datetime.now().isoformat().split('.')[0] + 'Z'
        return result