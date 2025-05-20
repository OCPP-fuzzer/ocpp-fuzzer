from ocpptypes.NetworkConnectionProfileType import NetworkConnectionProfileType


class SetNetworkProfileRequest:
    def __init__(self, configurationSlot: int, connectionData: NetworkConnectionProfileType):
        self.configurationSlot = configurationSlot
        self.connectionData = connectionData

    def to_dict(self):
        request = {
            "configurationSlot" : self.configurationSlot,
            "connectionData" : self.connectionData.to_dict(),
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['configurationSlot'] = 1
        result['connectionData'] = NetworkConnectionProfileType.sample(option=option)

        return result
    