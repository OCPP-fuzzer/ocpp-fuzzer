from enum import Enum
    
class DiagnosticsStatus(Enum):

    """
    EnumType class
    : Idle : Charge Point is not performing diagnostics related tasks. Status Idle SHALL only be used as in a DiagnosticsStatusNotification.req that was triggered by a TriggerMessage.req
    : Uploaded : Diagnostics information has been uploaded.
    : UploadFailed : Uploading of diagnostics failed.
    : Uploading : File is being uploaded.
    """

    IDLE = "Idle"
    UPLOADED = "Uploaded"
    UPLOADFAILED = "UploadFailed"
    UPLOADING = "Uploading"

    def get_value(self):
        return self.value

    @classmethod
    def get_members(cls):
        return [m for m in cls]

    @classmethod
    def get_sample(cls, option=False):
        value = __import__('random').choice(list(cls))
        return value.value
    