from typing import List, Optional

from ocpptypes.IdTokenType import IdTokenType
from ocpptypes.OCSPRequestDataType import OCSPRequestDataType


class AuthorizeRequest:
    def __init__(self, idToken: IdTokenType, certificate: Optional[str] = None, iso15118CertificateHashData: Optional[List[OCSPRequestDataType]] = None):
        self.idToken = idToken

        if certificate:
            self.certificate = certificate
        if iso15118CertificateHashData:
            self.iso15118CertificateHashData = iso15118CertificateHashData

    def to_dict(self):
        request = {
            "idToken" : self.idToken.to_dict(),
        }

        if self.certificate:
            request["certificate"] = self.certificate
        if self.iso15118CertificateHashData:
            request["iso15118CertificateHashData"] = [iso15118CertificateHashData.to_dict() for iso15118CertificateHashData in self.iso15118CertificateHashData]

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['idToken'] = IdTokenType.sample(option=option)

        if option:
            result['certificate'] = "string"
            result['iso15118CertificateHashData'] = [OCSPRequestDataType.sample(option=option)]

        return result
    