from typing import Optional, List

from ocppenum.ChargingProfilePurposeEnumType import ChargingProfilePurposeEnumType
from ocppenum.ChargingLimitSourceEnumType import ChargingLimitSourceEnumType


class ChargingProfileCriterionType:
    def __init__(self, chargingProfilePurpose: Optional[ChargingProfilePurposeEnumType] = None, stackLevel: Optional[int] = None, chargingProfileId: Optional[List[int]] = None, chargingLimitSource: Optional[List[ChargingLimitSourceEnumType]] = None):

        if chargingProfilePurpose:
            self.chargingProfilePurpose = chargingProfilePurpose
        if stackLevel:
            self.stackLevel = stackLevel
        if chargingProfileId:
            self.chargingProfileId = chargingProfileId
        if chargingLimitSource:
            self.chargingLimitSource = chargingLimitSource

    def to_dict(self):
        request = {
        }

        if self.chargingProfilePurpose:
            request["chargingProfilePurpose"] = self.chargingProfilePurpose.value
        if self.stackLevel:
            request["stackLevel"] = self.stackLevel
        if self.chargingProfileId:
            request["chargingProfileId"] = [chargingProfileId for chargingProfileId in self.chargingProfileId]
        if self.chargingLimitSource:
            request["chargingLimitSource"] = [chargingLimitSource.value for chargingLimitSource in self.chargingLimitSource]

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        if option:
            result['chargingProfilePurpose'] = ChargingProfilePurposeEnumType.sample()
            result['stackLevel'] = 1
            result['chargingProfileId'] = [1]
            result['chargingLimitSource'] = [ChargingLimitSourceEnumType.sample()]

        return result
    