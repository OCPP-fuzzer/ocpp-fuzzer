from enum import Enum
    
class MeasurandEnumType(Enum):
    CURRENT__EXPORT = "Current.Export" 
    CURRENT__IMPORT = "Current.Import" 
    CURRENT__OFFERED = "Current.Offered" 
    ENERGY__ACTIVE__EXPORT__REGISTER = "Energy.Active.Export.Register" 
    ENERGY__ACTIVE__IMPORT__REGISTER = "Energy.Active.Import.Register" 
    ENERGY__REACTIVE__EXPORT__REGISTER = "Energy.Reactive.Export.Register" 
    ENERGY__REACTIVE__IMPORT__REGISTER = "Energy.Reactive.Import.Register" 
    ENERGY__ACTIVE__EXPORT__INTERVAL = "Energy.Active.Export.Interval" 
    ENERGY__ACTIVE__IMPORT__INTERVAL = "Energy.Active.Import.Interval" 
    ENERGY__ACTIVE__NET = "Energy.Active.Net" 
    ENERGY__REACTIVE__EXPORT__INTERVAL = "Energy.Reactive.Export.Interval" 
    ENERGY__REACTIVE__IMPORT__INTERVAL = "Energy.Reactive.Import.Interval" 
    ENERGY__REACTIVE__NET = "Energy.Reactive.Net" 
    ENERGY__APPARENT__NET = "Energy.Apparent.Net" 
    ENERGY__APPARENT__IMPORT = "Energy.Apparent.Import" 
    ENERGY__APPARENT__EXPORT = "Energy.Apparent.Export" 
    FREQUENCY = "Frequency" 
    POWER__ACTIVE__EXPORT = "Power.Active.Export" 
    POWER__ACTIVE__IMPORT = "Power.Active.Import" 
    POWER__FACTOR = "Power.Factor" 
    POWER__OFFERED = "Power.Offered" 
    POWER__REACTIVE__EXPORT = "Power.Reactive.Export" 
    POWER__REACTIVE__IMPORT = "Power.Reactive.Import" 
    SO_C = "SoC" 
    VOLTAGE = "Voltage" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    