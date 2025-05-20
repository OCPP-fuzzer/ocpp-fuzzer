from typing import Optional

from ocppenum.OCPPVersionEnumType import OCPPVersionEnumType
from ocppenum.OCPPTransportEnumType import OCPPTransportEnumType
from ocppenum.OCPPInterfaceEnumType import OCPPInterfaceEnumType
from ocpptypes.VPNType import VPNType
from ocpptypes.APNType import APNType


class NetworkConnectionProfileType:
    def __init__(self, ocppVersion: OCPPVersionEnumType, ocppTransport: OCPPTransportEnumType, ocppCsmsUrl: str, messageTimeout: int, securityProfile: int, ocppInterface: OCPPInterfaceEnumType, vpn: Optional[VPNType] = None, apn: Optional[APNType] = None):
        self.ocppVersion = ocppVersion
        self.ocppTransport = ocppTransport
        self.ocppCsmsUrl = ocppCsmsUrl
        self.messageTimeout = messageTimeout
        self.securityProfile = securityProfile
        self.ocppInterface = ocppInterface

        if vpn:
            self.vpn = vpn
        if apn:
            self.apn = apn

    def to_dict(self):
        request = {
            "ocppVersion" : self.ocppVersion.value,
            "ocppTransport" : self.ocppTransport.value,
            "ocppCsmsUrl" : self.ocppCsmsUrl,
            "messageTimeout" : self.messageTimeout,
            "securityProfile" : self.securityProfile,
            "ocppInterface" : self.ocppInterface.value,
        }

        if self.vpn:
            request["vpn"] = self.vpn.to_dict()
        if self.apn:
            request["apn"] = self.apn.to_dict()

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['ocppVersion'] = OCPPVersionEnumType.sample()
        result['ocppTransport'] = OCPPTransportEnumType.sample()
        result['ocppCsmsUrl'] = "string"
        result['messageTimeout'] = 1
        result['securityProfile'] = 1
        result['ocppInterface'] = OCPPInterfaceEnumType.sample()

        if option:
            result['vpn'] = VPNType.sample(option=option)
            result['apn'] = APNType.sample(option=option)

        return result
    