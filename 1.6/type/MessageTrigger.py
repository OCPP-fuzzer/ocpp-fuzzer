from enum import Enum
    
class MessageTrigger(Enum):

    """
    EnumType class
    : BootNotification : To trigger a BootNotification request
    : DiagnosticsStatusNotification : To trigger a DiagnosticsStatusNotification request
    : FirmwareStatusNotification : To trigger a FirmwareStatusNotification request
    : Heartbeat : To trigger a Heartbeat request
    : MeterValues : To trigger a MeterValues request
    : StatusNotification : To trigger a StatusNotification request
    """

    BOOTNOTIFICATION = "BootNotification"
    DIAGNOSTICSSTATUSNOTIFICATION = "DiagnosticsStatusNotification"
    FIRMWARESTATUSNOTIFICATION = "FirmwareStatusNotification"
    HEARTBEAT = "Heartbeat"
    METERVALUES = "MeterValues"
    STATUSNOTIFICATION = "StatusNotification"

    def get_value(self):
        return self.value

    @classmethod
    def get_members(cls):
        return [m for m in cls]

    @classmethod
    def get_sample(cls, option=False):
        value = __import__('random').choice(list(cls))
        return value.value
    