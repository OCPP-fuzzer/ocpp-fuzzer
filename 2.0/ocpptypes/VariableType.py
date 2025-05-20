from typing import Optional

identifierString = str

class VariableType:
    def __init__(self, name: identifierString, instance: Optional[identifierString] = None):
        self.name = name

        if instance:
            self.instance = instance

    def to_dict(self):
        request = {
            "name" : self.name,
        }

        if self.instance:
            request["instance"] = self.instance

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['name'] = str(__import__('uuid').uuid4())

        if option:
            result['instance'] = str(__import__('uuid').uuid4())

        return result
    