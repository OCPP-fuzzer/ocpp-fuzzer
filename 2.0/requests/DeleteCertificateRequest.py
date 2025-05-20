from ocpptypes.CertificateHashDataType import CertificateHashDataType


class DeleteCertificateRequest:
    def __init__(self, certificateHashData: CertificateHashDataType):
        self.certificateHashData = certificateHashData

    def to_dict(self):
        request = {
            "certificateHashData" : self.certificateHashData.to_dict(),
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['certificateHashData'] = CertificateHashDataType.sample(option=option)

        return result
    