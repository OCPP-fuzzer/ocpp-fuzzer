from enum import Enum
    
class Location(Enum):

    """
    EnumType class
    : Body : Measurement inside body of Charge Point (e.g. Temperature)
    : Cable : Measurement taken from cable between EV and Charge Point
    : EV : Measurement taken by EV
    : Inlet : Measurement at network (“grid”) inlet connection
    : Outlet : Measurement at a Connector. Default value
    """

    BODY = "Body"
    CABLE = "Cable"
    EV = "EV"
    INLET = "Inlet"
    OUTLET = "Outlet"

    def get_value(self):
        return self.value

    @classmethod
    def get_members(cls):
        return [m for m in cls]

    @classmethod
    def get_sample(cls, option=False):
        value = __import__('random').choice(list(cls))
        return value.value
    