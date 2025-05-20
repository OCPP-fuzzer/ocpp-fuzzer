
class CancelReservationRequest:

    def __init__(self, reservationId: int):
        self.reservationId = reservationId

    def get_value(self):
        result = {
            "reservationId" : self.reservationId,
        }
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['reservationId'] = 1
        return result