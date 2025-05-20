from type.AvailabilityType import AvailabilityType

class ChangeAvailabilityRequest:

    def __init__(self, connectorId: int, type: AvailabilityType):
        self.connectorId = connectorId
        self.type = type

    def get_value(self):
        result = {
            "connectorId" : self.connectorId,
            "type" : self.type.get_value(),
        }
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['connectorId'] = 1
        result['type'] = AvailabilityType.get_sample(option=option)
        return result