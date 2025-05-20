from ocppenum.BootReasonEnumType import BootReasonEnumType
from ocpptypes.ChargingStationType import ChargingStationType


class BootNotificationRequest:
    def __init__(self, reason: BootReasonEnumType, chargingStation: ChargingStationType):
        self.reason = reason
        self.chargingStation = chargingStation

    def to_dict(self):
        request = {
            "reason" : self.reason.value,
            "chargingStation" : self.chargingStation.to_dict(),
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['reason'] = BootReasonEnumType.sample()
        result['chargingStation'] = ChargingStationType.sample(option=option)

        return result
    