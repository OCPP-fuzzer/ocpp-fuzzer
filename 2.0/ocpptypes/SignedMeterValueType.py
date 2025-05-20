
class SignedMeterValueType:
    def __init__(self, signedMeterData: str, signingMethod: str, encodingMethod: str, publicKey: str):
        self.signedMeterData = signedMeterData
        self.signingMethod = signingMethod
        self.encodingMethod = encodingMethod
        self.publicKey = publicKey

    def to_dict(self):
        request = {
            "signedMeterData" : self.signedMeterData,
            "signingMethod" : self.signingMethod,
            "encodingMethod" : self.encodingMethod,
            "publicKey" : self.publicKey,
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['signedMeterData'] = "string"
        result['signingMethod'] = "string"
        result['encodingMethod'] = "string"
        result['publicKey'] = "string"

        return result
    