from typing import Optional, List

from datetime import datetime

from ocppenum.ChargingProfilePurposeEnumType import ChargingProfilePurposeEnumType
from ocppenum.ChargingProfileKindEnumType import ChargingProfileKindEnumType
from ocppenum.RecurrencyKindEnumType import RecurrencyKindEnumType
from ocpptypes.ChargingScheduleType import ChargingScheduleType

identifierString = str

class ChargingProfileType:
    def __init__(self, id: int, stackLevel: int, chargingProfilePurpose: ChargingProfilePurposeEnumType, chargingProfileKind: ChargingProfileKindEnumType, chargingSchedule: List[ChargingScheduleType], recurrencyKind: Optional[RecurrencyKindEnumType] = None, validFrom: Optional[datetime] = None, validTo: Optional[datetime] = None, transactionId: Optional[identifierString] = None):
        self.id = id
        self.stackLevel = stackLevel
        self.chargingProfilePurpose = chargingProfilePurpose
        self.chargingProfileKind = chargingProfileKind
        self.chargingSchedule = chargingSchedule

        if recurrencyKind:
            self.recurrencyKind = recurrencyKind
        if validFrom:
            self.validFrom = validFrom
        if validTo:
            self.validTo = validTo
        if transactionId:
            self.transactionId = transactionId

    def to_dict(self):
        request = {
            "id" : self.id,
            "stackLevel" : self.stackLevel,
            "chargingProfilePurpose" : self.chargingProfilePurpose.value,
            "chargingProfileKind" : self.chargingProfileKind.value,
            "chargingSchedule" : [chargingSchedule.to_dict() for chargingSchedule in self.chargingSchedule],
        }

        if self.recurrencyKind:
            request["recurrencyKind"] = self.recurrencyKind.value
        if self.validFrom:
            request["validFrom"] = self.validFrom.isoformat().split('.')[0] + 'Z'
        if self.validTo:
            request["validTo"] = self.validTo.isoformat().split('.')[0] + 'Z'
        if self.transactionId:
            request["transactionId"] = self.transactionId

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['id'] = 1
        result['stackLevel'] = 1
        result['chargingProfilePurpose'] = ChargingProfilePurposeEnumType.sample()
        result['chargingProfileKind'] = ChargingProfileKindEnumType.sample()
        result['chargingSchedule'] = [ChargingScheduleType.sample(option=option)]

        if option:
            result['recurrencyKind'] = RecurrencyKindEnumType.sample()
            result['validFrom'] = datetime.now().isoformat().split('.')[0] + 'Z'
            result['validTo'] = datetime.now().isoformat().split('.')[0] + 'Z'
            result['transactionId'] = str(__import__('uuid').uuid4())

        return result
    