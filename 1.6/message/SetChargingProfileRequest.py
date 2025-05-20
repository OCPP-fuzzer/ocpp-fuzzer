from type.ChargingProfile import ChargingProfile

class SetChargingProfileRequest:

    def __init__(self, connectorId: int, csChargingProfiles: ChargingProfile):
        self.connectorId = connectorId
        self.csChargingProfiles = csChargingProfiles

    def get_value(self):
        result = {
            "connectorId" : self.connectorId,
            "csChargingProfiles" : self.csChargingProfiles.get_value(),
        }
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['connectorId'] = 1
        result['csChargingProfiles'] = ChargingProfile.get_sample(option=option)
        return result