
class CancelReservationRequest:
    def __init__(self, reservationId: int):
        self.reservationId = reservationId

    def to_dict(self):
        request = {
            "reservationId" : self.reservationId,
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['reservationId'] = 1

        return result
    