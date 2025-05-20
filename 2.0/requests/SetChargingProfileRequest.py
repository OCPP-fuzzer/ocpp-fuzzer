from ocpptypes.ChargingProfileType import ChargingProfileType


class SetChargingProfileRequest:
    def __init__(self, evseId: int, chargingProfile: ChargingProfileType):
        self.evseId = evseId
        self.chargingProfile = chargingProfile

    def to_dict(self):
        request = {
            "evseId" : self.evseId,
            "chargingProfile" : self.chargingProfile.to_dict(),
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['evseId'] = 1
        result['chargingProfile'] = ChargingProfileType.sample(option=option)

        return result
    