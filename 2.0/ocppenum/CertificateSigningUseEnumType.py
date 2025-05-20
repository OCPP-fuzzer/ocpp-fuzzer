from enum import Enum
    
class CertificateSigningUseEnumType(Enum):
    CHARGING_STATION_CERTIFICATE = "ChargingStationCertificate" 
    V2_G_CERTIFICATE = "V2GCertificate" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    