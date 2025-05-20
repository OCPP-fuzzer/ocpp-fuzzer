from type.ChargingProfileStatus import ChargingProfileStatus

class SetChargingProfileResponse:

    def __init__(self, status: ChargingProfileStatus):
        self.status = status

    def get_value(self):
        result = {
            "status" : self.status.get_value(),
        }
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['status'] = ChargingProfileStatus.get_sample(option=option)
        return result