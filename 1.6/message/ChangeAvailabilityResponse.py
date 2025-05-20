from type.AvailabilityStatus import AvailabilityStatus

class ChangeAvailabilityResponse:

    def __init__(self, status: AvailabilityStatus):
        self.status = status

    def get_value(self):
        result = {
            "status" : self.status.get_value(),
        }
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['status'] = AvailabilityStatus.get_sample(option=option)
        return result