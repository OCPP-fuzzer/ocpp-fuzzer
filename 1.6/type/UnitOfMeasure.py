from enum import Enum
    
class UnitOfMeasure(Enum):

    """
    EnumType class
    : Wh : Watt-hours (energy). Default.
    : kWh : kiloWatt-hours (energy).
    : varh : Var-hours (reactive energy).
    : kvarh : kilovar-hours (reactive energy).
    : W : Watts (power).
    : kW : kilowatts (power).
    : VA : VoltAmpere (apparent power).
    : kVA : kiloVolt Ampere (apparent power).
    : var : Vars (reactive power).
    : kvar : kilovars (reactive power).
    : A : Amperes (current).
    : V : Voltage (r.m.s. AC).
    : Celsius : Degrees (temperature).
    : Fahrenheit : Degrees (temperature).
    : K : Degrees Kelvin (temperature).
    : Percent : Percentage.
    """

    WH = "Wh"
    KWH = "kWh"
    VARH = "varh"
    KVARH = "kvarh"
    W = "W"
    KW = "kW"
    VA = "VA"
    KVA = "kVA"
    VAR = "var"
    KVAR = "kvar"
    A = "A"
    V = "V"
    CELSIUS = "Celsius"
    FAHRENHEIT = "Fahrenheit"
    K = "K"
    PERCENT = "Percent"

    def get_value(self):
        return self.value

    @classmethod
    def get_members(cls):
        return [m for m in cls]

    @classmethod
    def get_sample(cls, option=False):
        value = __import__('random').choice(list(cls))
        return value.value
    