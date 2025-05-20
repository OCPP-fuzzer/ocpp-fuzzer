from typing import Optional

from ocpptypes.ModemType import ModemType


class ChargingStationType:
    def __init__(self, model: str, vendorName: str, serialNumber: Optional[str] = None, firmwareVersion: Optional[str] = None, modem: Optional[ModemType] = None):
        self.model = model
        self.vendorName = vendorName

        if serialNumber:
            self.serialNumber = serialNumber
        if firmwareVersion:
            self.firmwareVersion = firmwareVersion
        if modem:
            self.modem = modem

    def to_dict(self):
        request = {
            "model" : self.model,
            "vendorName" : self.vendorName,
        }

        if self.serialNumber:
            request["serialNumber"] = self.serialNumber
        if self.firmwareVersion:
            request["firmwareVersion"] = self.firmwareVersion
        if self.modem:
            request["modem"] = self.modem.to_dict()

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['model'] = "string"
        result['vendorName'] = "string"

        if option:
            result['serialNumber'] = "string"
            result['firmwareVersion'] = "string"
            result['modem'] = ModemType.sample(option=option)

        return result
    