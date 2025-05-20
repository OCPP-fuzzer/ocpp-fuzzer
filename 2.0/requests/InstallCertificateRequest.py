from ocppenum.InstallCertificateUseEnumType import InstallCertificateUseEnumType


class InstallCertificateRequest:
    def __init__(self, certificateType: InstallCertificateUseEnumType, certificate: str):
        self.certificateType = certificateType
        self.certificate = certificate

    def to_dict(self):
        request = {
            "certificateType" : self.certificateType.value,
            "certificate" : self.certificate,
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['certificateType'] = InstallCertificateUseEnumType.sample()
        result['certificate'] = "string"

        return result
    