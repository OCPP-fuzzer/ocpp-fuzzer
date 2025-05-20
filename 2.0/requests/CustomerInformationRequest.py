from typing import Optional

from ocpptypes.IdTokenType import IdTokenType
from ocpptypes.CertificateHashDataType import CertificateHashDataType


class CustomerInformationRequest:
    def __init__(self, requestId: int, report: bool, clear: bool, customerIdentifier: Optional[str] = None, idToken: Optional[IdTokenType] = None, customerCertificate: Optional[CertificateHashDataType] = None):
        self.requestId = requestId
        self.report = report
        self.clear = clear

        if customerIdentifier:
            self.customerIdentifier = customerIdentifier
        if idToken:
            self.idToken = idToken
        if customerCertificate:
            self.customerCertificate = customerCertificate

    def to_dict(self):
        request = {
            "requestId" : self.requestId,
            "report" : self.report,
            "clear" : self.clear,
        }

        if self.customerIdentifier:
            request["customerIdentifier"] = self.customerIdentifier
        if self.idToken:
            request["idToken"] = self.idToken.to_dict()
        if self.customerCertificate:
            request["customerCertificate"] = self.customerCertificate.to_dict()

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['requestId'] = 1
        result['report'] = True
        result['clear'] = True

        if option:
            result['customerIdentifier'] = "string"
            result['idToken'] = IdTokenType.sample(option=option)
            result['customerCertificate'] = CertificateHashDataType.sample(option=option)

        return result
    