from type.CancelReservationStatus import CancelReservationStatus

class CancelReservationResponse:

    def __init__(self, status: CancelReservationStatus):
        self.status = status

    def get_value(self):
        result = {
            "status" : self.status.get_value(),
        }
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['status'] = CancelReservationStatus.get_sample(option=option)
        return result