from ocpptypes.MessageInfoType import MessageInfoType


class SetDisplayMessageRequest:
    def __init__(self, message: MessageInfoType):
        self.message = message

    def to_dict(self):
        request = {
            "message" : self.message.to_dict(),
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['message'] = MessageInfoType.sample(option=option)

        return result
    