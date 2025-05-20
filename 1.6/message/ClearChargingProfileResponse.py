from type.ClearChargingProfileStatus import ClearChargingProfileStatus

class ClearChargingProfileResponse:

    def __init__(self, status: ClearChargingProfileStatus):
        self.status = status

    def get_value(self):
        result = {
            "status" : self.status.get_value(),
        }
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['status'] = ClearChargingProfileStatus.get_sample(option=option)
        return result