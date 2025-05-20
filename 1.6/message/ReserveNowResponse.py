from type.ReservationStatus import ReservationStatus

class ReserveNowResponse:

    def __init__(self, status: ReservationStatus):
        self.status = status

    def get_value(self):
        result = {
            "status" : self.status.get_value(),
        }
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['status'] = ReservationStatus.get_sample(option=option)
        return result