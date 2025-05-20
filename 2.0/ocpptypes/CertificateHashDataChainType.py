from typing import Optional, List

from ocppenum.GetCertificateIdUseEnumType import GetCertificateIdUseEnumType
from ocpptypes.CertificateHashDataType import CertificateHashDataType
from ocpptypes.CertificateHashDataType import CertificateHashDataType


class CertificateHashDataChainType:
    def __init__(self, certificateType: GetCertificateIdUseEnumType, certificateHashData: CertificateHashDataType, childCertificateHashData: Optional[List[CertificateHashDataType]] = None):
        self.certificateType = certificateType
        self.certificateHashData = certificateHashData

        if childCertificateHashData:
            self.childCertificateHashData = childCertificateHashData

    def to_dict(self):
        request = {
            "certificateType" : self.certificateType.value,
            "certificateHashData" : self.certificateHashData.to_dict(),
        }

        if self.childCertificateHashData:
            request["childCertificateHashData"] = [childCertificateHashData.to_dict() for childCertificateHashData in self.childCertificateHashData]

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['certificateType'] = GetCertificateIdUseEnumType.sample()
        result['certificateHashData'] = CertificateHashDataType.sample(option=option)

        if option:
            result['childCertificateHashData'] = [CertificateHashDataType.sample(option=option)]

        return result
    