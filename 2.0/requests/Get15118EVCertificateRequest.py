from ocppenum.CertificateActionEnumType import CertificateActionEnumType


class Get15118EVCertificateRequest:
    def __init__(self, iso15118SchemaVersion: str, action: CertificateActionEnumType, exiRequest: str):
        self.iso15118SchemaVersion = iso15118SchemaVersion
        self.action = action
        self.exiRequest = exiRequest

    def to_dict(self):
        request = {
            "iso15118SchemaVersion" : self.iso15118SchemaVersion,
            "action" : self.action.value,
            "exiRequest" : self.exiRequest,
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['iso15118SchemaVersion'] = "string"
        result['action'] = CertificateActionEnumType.sample()
        result['exiRequest'] = "string"

        return result
    