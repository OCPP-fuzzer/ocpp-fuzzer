from typing import Optional

from ocppenum.APNAuthenticationEnumType import APNAuthenticationEnumType

idetifierString = str

class APNType:
    def __init__(self, apn: str, apnAuthentication: APNAuthenticationEnumType, apnUserName: Optional[str] = None, apnPassword: Optional[str] = None, simPin: Optional[int] = None, preferredNetwork: Optional[idetifierString] = None, useOnlyPreferredNetwork: Optional[bool] = None):
        self.apn = apn
        self.apnAuthentication = apnAuthentication

        if apnUserName:
            self.apnUserName = apnUserName
        if apnPassword:
            self.apnPassword = apnPassword
        if simPin:
            self.simPin = simPin
        if preferredNetwork:
            self.preferredNetwork = preferredNetwork
        if useOnlyPreferredNetwork:
            self.useOnlyPreferredNetwork = useOnlyPreferredNetwork

    def to_dict(self):
        request = {
            "apn" : self.apn,
            "apnAuthentication" : self.apnAuthentication.value,
        }

        if self.apnUserName:
            request["apnUserName"] = self.apnUserName
        if self.apnPassword:
            request["apnPassword"] = self.apnPassword
        if self.simPin:
            request["simPin"] = self.simPin
        if self.preferredNetwork:
            request["preferredNetwork"] = self.preferredNetwork
        if self.useOnlyPreferredNetwork:
            request["useOnlyPreferredNetwork"] = self.useOnlyPreferredNetwork

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['apn'] = "string"
        result['apnAuthentication'] = APNAuthenticationEnumType.sample()

        if option:
            result['apnUserName'] = "string"
            result['apnPassword'] = "string"
            result['simPin'] = 1
            result['preferredNetwork'] = str(__import__('uuid').uuid4())
            result['useOnlyPreferredNetwork'] = True

        return result
    