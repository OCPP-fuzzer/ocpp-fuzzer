from ocpptypes.OCSPRequestDataType import OCSPRequestDataType


class GetCertificateStatusRequest:
    def __init__(self, ocspRequestData: OCSPRequestDataType):
        self.ocspRequestData = ocspRequestData

    def to_dict(self):
        request = {
            "ocspRequestData" : self.ocspRequestData.to_dict(),
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['ocspRequestData'] = OCSPRequestDataType.sample(option=option)

        return result
    