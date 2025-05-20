from typing import Optional


class StatusInfoType:
    def __init__(self, reasonCode: str, additionalInfo: Optional[str] = None):
        self.reasonCode = reasonCode

        if additionalInfo:
            self.additionalInfo = additionalInfo

    def to_dict(self):
        request = {
            "reasonCode" : self.reasonCode,
        }

        if self.additionalInfo:
            request["additionalInfo"] = self.additionalInfo

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['reasonCode'] = "string"

        if option:
            result['additionalInfo'] = "string"

        return result
    