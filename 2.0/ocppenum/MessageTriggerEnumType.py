from enum import Enum
    
class MessageTriggerEnumType(Enum):
    BOOT_NOTIFICATION = "BootNotification" 
    LOG_STATUS_NOTIFICATION = "LogStatusNotification" 
    FIRMWARE_STATUS_NOTIFICATION = "FirmwareStatusNotification" 
    HEARTBEAT = "Heartbeat" 
    METER_VALUES = "MeterValues" 
    SIGN_CHARGING_STATION_CERTIFICATE = "SignChargingStationCertificate" 
    SIGN_V2_G_CERTIFICATE = "SignV2GCertificate" 
    STATUS_NOTIFICATION = "StatusNotification" 
    TRANSACTION_EVENT = "TransactionEvent" 
    SIGN_COMBINED_CERTIFICATE = "SignCombinedCertificate" 
    PUBLISH_FIRMWARE_STATUS_NOTIFICATION = "PublishFirmwareStatusNotification" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    