from typing import Optional

from ocppenum.AttributeEnumType import AttributeEnumType
from ocppenum.MutabilityEnumType import MutabilityEnumType


class VariableAttributeType:
    def __init__(self, ype: Optional[AttributeEnumType] = None, value: Optional[str] = None, mutability: Optional[MutabilityEnumType] = None, persistent: Optional[bool] = None, constant: Optional[bool] = None):

        if ype:
            self.ype = ype
        if value:
            self.value = value
        if mutability:
            self.mutability = mutability
        if persistent:
            self.persistent = persistent
        if constant:
            self.constant = constant

    def to_dict(self):
        request = {
        }

        if self.ype:
            request["ype"] = self.ype.value
        if self.value:
            request["value"] = self.value
        if self.mutability:
            request["mutability"] = self.mutability.value
        if self.persistent:
            request["persistent"] = self.persistent
        if self.constant:
            request["constant"] = self.constant

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        if option:
            result['ype'] = AttributeEnumType.sample()
            result['value'] = "string"
            result['mutability'] = MutabilityEnumType.sample()
            result['persistent'] = True
            result['constant'] = True

        return result
    