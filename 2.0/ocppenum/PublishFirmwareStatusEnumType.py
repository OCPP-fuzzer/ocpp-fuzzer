from enum import Enum
    
class PublishFirmwareStatusEnumType(Enum):
    IDLE = "Idle" 
    DOWNLOAD_SCHEDULED = "DownloadScheduled" 
    DOWNLOADING = "Downloading" 
    DOWNLOADED = "Downloaded" 
    PUBLISHED = "Published" 
    DOWNLOAD_FAILED = "DownloadFailed" 
    DOWNLOAD_PAUSED = "DownloadPaused" 
    INVALID_CHECKSUM = "InvalidChecksum" 
    CHECKSUM_VERIFIED = "ChecksumVerified" 
    PUBLISH_FAILED = "PublishFailed" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    