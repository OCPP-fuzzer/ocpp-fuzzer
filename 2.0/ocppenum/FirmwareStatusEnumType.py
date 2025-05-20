from enum import Enum
    
class FirmwareStatusEnumType(Enum):
    DOWNLOADED = "Downloaded" 
    DOWNLOAD_FAILED = "DownloadFailed" 
    DOWNLOADING = "Downloading" 
    DOWNLOAD_SCHEDULED = "DownloadScheduled" 
    DOWNLOAD_PAUSED = "DownloadPaused" 
    IDLE = "Idle" 
    INSTALLATION_FAILED = "InstallationFailed" 
    INSTALLING = "Installing" 
    INSTALLED = "Installed" 
    INSTALL_REBOOTING = "InstallRebooting" 
    INSTALL_SCHEDULED = "InstallScheduled" 
    INSTALL_VERIFICATION_FAILED = "InstallVerificationFailed" 
    INVALID_SIGNATURE = "InvalidSignature" 
    SIGNATURE_VERIFIED = "SignatureVerified" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    