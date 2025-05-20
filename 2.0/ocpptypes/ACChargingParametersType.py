
class ACChargingParametersType:
    def __init__(self, energyAmount: int, evMinCurrent: int, evMaxCurrent: int, evMaxVoltage: int):
        self.energyAmount = energyAmount
        self.evMinCurrent = evMinCurrent
        self.evMaxCurrent = evMaxCurrent
        self.evMaxVoltage = evMaxVoltage

    def to_dict(self):
        request = {
            "energyAmount" : self.energyAmount,
            "evMinCurrent" : self.evMinCurrent,
            "evMaxCurrent" : self.evMaxCurrent,
            "evMaxVoltage" : self.evMaxVoltage,
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['energyAmount'] = 1
        result['evMinCurrent'] = 1
        result['evMaxCurrent'] = 1
        result['evMaxVoltage'] = 1

        return result
    