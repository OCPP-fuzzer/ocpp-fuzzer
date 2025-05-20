from typing import Optional

from ocppenum.MessageTriggerEnumType import MessageTriggerEnumType
from ocpptypes.EVSEType import EVSEType


class TriggerMessageRequest:
    def __init__(self, requestedMessage: MessageTriggerEnumType, evse: Optional[EVSEType] = None):
        self.requestedMessage = requestedMessage

        if evse:
            self.evse = evse

    def to_dict(self):
        request = {
            "requestedMessage" : self.requestedMessage.value,
        }

        if self.evse:
            request["evse"] = self.evse.to_dict()

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['requestedMessage'] = MessageTriggerEnumType.sample()

        if option:
            result['evse'] = EVSEType.sample(option=option)

        return result
    