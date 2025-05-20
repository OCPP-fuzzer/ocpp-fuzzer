from typing import Optional

from ocppenum.CertificateSigningUseEnumType import CertificateSigningUseEnumType


class SignCertificateRequest:
    def __init__(self, csr: str, certificateType: Optional[CertificateSigningUseEnumType] = None):
        self.csr = csr

        if certificateType:
            self.certificateType = certificateType

    def to_dict(self):
        request = {
            "csr" : self.csr,
        }

        if self.certificateType:
            request["certificateType"] = self.certificateType.value

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['csr'] = "string"

        if option:
            result['certificateType'] = CertificateSigningUseEnumType.sample()

        return result
    