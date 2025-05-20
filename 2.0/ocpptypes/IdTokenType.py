from typing import Optional, List

from ocppenum.IdTokenEnumType import IdTokenEnumType
from ocpptypes.AdditionalInfoType import AdditionalInfoType

identifierString = str

class IdTokenType:
    def __init__(self, idToken: identifierString, type: IdTokenEnumType, additionalInfo: Optional[List[AdditionalInfoType]] = None):
        self.idToken = idToken
        self.type = type

        if additionalInfo:
            self.additionalInfo = additionalInfo

    def to_dict(self):
        request = {
            "idToken" : self.idToken,
            "type" : self.type.value,
        }

        if self.additionalInfo:
            request["additionalInfo"] = [additionalInfo.to_dict() for additionalInfo in self.additionalInfo]

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['idToken'] = str(__import__('uuid').uuid4())
        result['type'] = IdTokenEnumType.sample()

        if option:
            result['additionalInfo'] = [AdditionalInfoType.sample(option=option)]

        return result
    