from enum import Enum
    
class Measurand(Enum):

    """
    EnumType class
    : Frequency : Instantaneous reading of powerline frequency. NOTE: OCPP 1.6 does not have a UnitOfMeasure for frequency, the UnitOfMeasure for any SampledValue with measurand: Frequency is Hertz.
    : RPM : Fan speed in RPM
    : SoC : State of charge of charging vehicle in percentage
    : Temperature : Temperature reading inside Charge Point.
    : Voltage : Instantaneous AC RMS supply voltage
    """

    FREQUENCY = "Frequency"
    RPM = "RPM"
    SOC = "SoC"
    TEMPERATURE = "Temperature"
    VOLTAGE = "Voltage"

    def get_value(self):
        return self.value

    @classmethod
    def get_members(cls):
        return [m for m in cls]

    @classmethod
    def get_sample(cls, option=False):
        value = __import__('random').choice(list(cls))
        return value.value
    