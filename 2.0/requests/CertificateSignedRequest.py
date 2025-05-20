from typing import Optional

from ocppenum.CertificateSigningUseEnumType import CertificateSigningUseEnumType


class CertificateSignedRequest:
    def __init__(self, certificateChain: str, certificateType: Optional[CertificateSigningUseEnumType] = None):
        self.certificateChain = certificateChain

        if certificateType:
            self.certificateType = certificateType

    def to_dict(self):
        request = {
            "certificateChain" : self.certificateChain,
        }

        if self.certificateType:
            request["certificateType"] = self.certificateType.value

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['certificateChain'] = "string"

        if option:
            result['certificateType'] = CertificateSigningUseEnumType.sample()

        return result
    