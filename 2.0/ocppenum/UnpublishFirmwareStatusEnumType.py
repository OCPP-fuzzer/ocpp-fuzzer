from enum import Enum
    
class UnpublishFirmwareStatusEnumType(Enum):
    DOWNLOAD_ONGOING = "DownloadOngoing" 
    NO_FIRMWARE = "NoFirmware" 
    UNPUBLISHED = "Unpublished" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    