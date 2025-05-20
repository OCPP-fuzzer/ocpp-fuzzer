from type.ConfigurationStatus import ConfigurationStatus

class ChangeConfigurationResponse:

    def __init__(self, status: ConfigurationStatus):
        self.status = status

    def get_value(self):
        result = {
            "status" : self.status.get_value(),
        }
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['status'] = ConfigurationStatus.get_sample(option=option)
        return result