from typing import List, Optional

from ocppenum.GetCertificateIdUseEnumType import GetCertificateIdUseEnumType


class GetInstalledCertificateIdsRequest:
    def __init__(self, certificateType: Optional[List[GetCertificateIdUseEnumType]] = None):

        if certificateType:
            self.certificateType = certificateType

    def to_dict(self):
        request = {
        }

        if self.certificateType:
            request["certificateType"] = [certificateType.value for certificateType in self.certificateType]

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        if option:
            result['certificateType'] = [GetCertificateIdUseEnumType.sample()]

        return result
    