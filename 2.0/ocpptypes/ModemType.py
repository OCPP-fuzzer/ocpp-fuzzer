from typing import Optional

identifierString = str

class ModemType:
    def __init__(self, iccid: Optional[identifierString] = None, imsi: Optional[identifierString] = None):

        if iccid:
            self.iccid = iccid
        if imsi:
            self.imsi = imsi

    def to_dict(self):
        request = {
        }

        if self.iccid:
            request["iccid"] = self.iccid
        if self.imsi:
            request["imsi"] = self.imsi

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        if option:
            result['iccid'] = str(__import__('uuid').uuid4())
            result['imsi'] = str(__import__('uuid').uuid4())

        return result
    