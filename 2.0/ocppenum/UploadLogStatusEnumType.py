from enum import Enum
    
class UploadLogStatusEnumType(Enum):
    BAD_MESSAGE = "BadMessage" 
    IDLE = "Idle" 
    NOT_SUPPORTED_OPERATION = "NotSupportedOperation" 
    PERMISSION_DENIED = "PermissionDenied" 
    UPLOADED = "Uploaded" 
    UPLOAD_FAILURE = "UploadFailure" 
    UPLOADING = "Uploading" 
    ACCEPTED_CANCELED = "AcceptedCanceled" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    