from ocppenum.ReservationUpdateStatusEnumType import ReservationUpdateStatusEnumType


class ReservationStatusUpdateRequest:
    def __init__(self, reservationId: int, reservationUpdateStatus: ReservationUpdateStatusEnumType):
        self.reservationId = reservationId
        self.reservationUpdateStatus = reservationUpdateStatus

    def to_dict(self):
        request = {
            "reservationId" : self.reservationId,
            "reservationUpdateStatus" : self.reservationUpdateStatus.value,
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['reservationId'] = 1
        result['reservationUpdateStatus'] = ReservationUpdateStatusEnumType.sample()

        return result
    