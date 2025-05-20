from enum import Enum
    
class FirmwareStatus(Enum):

    """
    EnumType class
    : Downloaded : New firmware has been downloaded by Charge Point.
    : DownloadFailed : Charge point failed to download firmware.
    : Downloading : Firmware is being downloaded.
    : Idle : Charge Point is not performing firmware update related tasks. Status Idle SHALL only be used as in a FirmwareStatusNotification.req that was triggered by a TriggerMessage.req
    : InstallationFailed : Installation of new firmware has failed.
    : Installing : Firmware is being installed.
    : Installed : New firmware has successfully been installed in charge point.
    """

    DOWNLOADED = "Downloaded"
    DOWNLOADFAILED = "DownloadFailed"
    DOWNLOADING = "Downloading"
    IDLE = "Idle"
    INSTALLATIONFAILED = "InstallationFailed"
    INSTALLING = "Installing"
    INSTALLED = "Installed"

    def get_value(self):
        return self.value

    @classmethod
    def get_members(cls):
        return [m for m in cls]

    @classmethod
    def get_sample(cls, option=False):
        value = __import__('random').choice(list(cls))
        return value.value
    