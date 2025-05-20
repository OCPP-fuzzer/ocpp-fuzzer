from enum import Enum
    
class ChargePointErrorCode(Enum):

    """
    EnumType class
    : ConnectorLockFailure : Failure to lock or unlock connector.
    : EVCommunicationError : Communication failure with the vehicle, might be Mode 3 or other communication protocol problem. This is not a real error in the sense that the Charge Point doesn’t need to go to the faulted state. Instead, it should go to the SuspendedEVSE state.
    : GroundFailure : Ground fault circuit interrupter has been activated.
    : HighTemperature : Temperature inside Charge Point is too high.
    : InternalError : Error in internal hard- or software component.
    : LocalListConflict : The authorization information received from the Central System is in conflict with the LocalAuthorizationList.
    : NoError : No error to report.
    : OtherError : Other type of error. More information in vendorErrorCode.
    : OverCurrentFailure : Over current protection device has tripped.
    : OverVoltage : Voltage has risen above an acceptable level.
    : PowerMeterFailure : Failure to read electrical/energy/power meter.
    : PowerSwitchFailure : Failure to control power switch.
    : ReaderFailure : Failure with idTag reader.
    : ResetFailure : Unable to perform a reset.
    : UnderVoltage : Voltage has dropped below an acceptable level.
    : WeakSignal : Wireless communication device reports a weak signal.
    """

    CONNECTORLOCKFAILURE = "ConnectorLockFailure"
    EVCOMMUNICATIONERROR = "EVCommunicationError"
    GROUNDFAILURE = "GroundFailure"
    HIGHTEMPERATURE = "HighTemperature"
    INTERNALERROR = "InternalError"
    LOCALLISTCONFLICT = "LocalListConflict"
    NOERROR = "NoError"
    OTHERERROR = "OtherError"
    OVERCURRENTFAILURE = "OverCurrentFailure"
    OVERVOLTAGE = "OverVoltage"
    POWERMETERFAILURE = "PowerMeterFailure"
    POWERSWITCHFAILURE = "PowerSwitchFailure"
    READERFAILURE = "ReaderFailure"
    RESETFAILURE = "ResetFailure"
    UNDERVOLTAGE = "UnderVoltage"
    WEAKSIGNAL = "WeakSignal"

    def get_value(self):
        return self.value

    @classmethod
    def get_members(cls):
        return [m for m in cls]

    @classmethod
    def get_sample(cls, option=False):
        value = __import__('random').choice(list(cls))
        return value.value
    