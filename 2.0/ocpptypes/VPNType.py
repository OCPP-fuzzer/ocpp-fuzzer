from typing import Optional

from ocppenum.VPNEnumType import VPNEnumType


class VPNType:
    def __init__(self, server: str, user: str, password: str, key: str, type: VPNEnumType, group: Optional[str] = None):
        self.server = server
        self.user = user
        self.password = password
        self.key = key
        self.type = type

        if group:
            self.group = group

    def to_dict(self):
        request = {
            "server" : self.server,
            "user" : self.user,
            "password" : self.password,
            "key" : self.key,
            "type" : self.type.value,
        }

        if self.group:
            request["group"] = self.group

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['server'] = "string"
        result['user'] = "string"
        result['password'] = "string"
        result['key'] = "string"
        result['type'] = VPNEnumType.sample()

        if option:
            result['group'] = "string"

        return result
    