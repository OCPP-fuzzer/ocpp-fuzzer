from typing import Optional

from ocpptypes.EVSEType import EVSEType

identifierString = str

class ComponentType:
    def __init__(self, name: identifierString, instance: Optional[identifierString] = None, evse: Optional[EVSEType] = None):
        self.name = name

        if instance:
            self.instance = instance
        if evse:
            self.evse = evse

    def to_dict(self):
        request = {
            "name" : self.name,
        }

        if self.instance:
            request["instance"] = self.instance
        if self.evse:
            request["evse"] = self.evse.to_dict()

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['name'] = str(__import__('uuid').uuid4())

        if option:
            result['instance'] = str(__import__('uuid').uuid4())
            result['evse'] = EVSEType.sample(option=option)

        return result
    