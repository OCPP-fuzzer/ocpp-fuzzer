from ocppenum.UnpublishFirmwareStatusEnumType import UnpublishFirmwareStatusEnumType


class UpdateFirmwareRequest:
    def __init__(self, status: UnpublishFirmwareStatusEnumType):
        self.status = status

    def to_dict(self):
        request = {
            "status" : self.status.value,
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['status'] = UnpublishFirmwareStatusEnumType.sample()

        return result
    