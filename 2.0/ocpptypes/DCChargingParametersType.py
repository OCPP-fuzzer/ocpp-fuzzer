from typing import Optional


class DCChargingParametersType:
    def __init__(self, evMaxCurrent: int, evMaxVoltage: int, energyAmount: Optional[int] = None, evMaxPower: Optional[int] = None, stateOfCharge: Optional[int] = None, evEnergyCapacity: Optional[int] = None, fullSoC: Optional[int] = None, bulkSoC: Optional[int] = None):
        self.evMaxCurrent = evMaxCurrent
        self.evMaxVoltage = evMaxVoltage

        if energyAmount:
            self.energyAmount = energyAmount
        if evMaxPower:
            self.evMaxPower = evMaxPower
        if stateOfCharge:
            self.stateOfCharge = stateOfCharge
        if evEnergyCapacity:
            self.evEnergyCapacity = evEnergyCapacity
        if fullSoC:
            self.fullSoC = fullSoC
        if bulkSoC:
            self.bulkSoC = bulkSoC

    def to_dict(self):
        request = {
            "evMaxCurrent" : self.evMaxCurrent,
            "evMaxVoltage" : self.evMaxVoltage,
        }

        if self.energyAmount:
            request["energyAmount"] = self.energyAmount
        if self.evMaxPower:
            request["evMaxPower"] = self.evMaxPower
        if self.stateOfCharge:
            request["stateOfCharge"] = self.stateOfCharge
        if self.evEnergyCapacity:
            request["evEnergyCapacity"] = self.evEnergyCapacity
        if self.fullSoC:
            request["fullSoC"] = self.fullSoC
        if self.bulkSoC:
            request["bulkSoC"] = self.bulkSoC

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['evMaxCurrent'] = 1
        result['evMaxVoltage'] = 1

        if option:
            result['energyAmount'] = 1
            result['evMaxPower'] = 1
            result['stateOfCharge'] = 1
            result['evEnergyCapacity'] = 1
            result['fullSoC'] = 1
            result['bulkSoC'] = 1

        return result
    