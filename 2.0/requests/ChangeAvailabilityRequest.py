from typing import Optional

from ocppenum.OperationalStatusEnumType import OperationalStatusEnumType
from ocpptypes.EVSEType import EVSEType


class ChangeAvailabilityRequest:
    def __init__(self, operationalStatus: OperationalStatusEnumType, evse: Optional[EVSEType] = None):
        self.operationalStatus = operationalStatus

        if evse:
            self.evse = evse

    def to_dict(self):
        request = {
            "operationalStatus" : self.operationalStatus.value,
        }

        if self.evse:
            request["evse"] = self.evse.to_dict()

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['operationalStatus'] = OperationalStatusEnumType.sample()

        if option:
            result['evse'] = EVSEType.sample(option=option)

        return result
    