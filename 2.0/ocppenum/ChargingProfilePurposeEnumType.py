from enum import Enum
    
class ChargingProfilePurposeEnumType(Enum):
    CHARGING_STATION_EXTERNAL_CONSTRAINTS = "ChargingStationExternalConstraints" 
    CHARGING_STATION_MAX_PROFILE = "ChargingStationMaxProfile" 
    TX_DEFAULT_PROFILE = "TxDefaultProfile" 
    TX_PROFILE = "TxProfile" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    