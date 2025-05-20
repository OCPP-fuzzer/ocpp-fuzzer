from typing import Optional

from type.MessageTrigger import MessageTrigger

class TriggerMessageRequest:

    def __init__(self, requestedMessage: MessageTrigger, connectorId: Optional[int]= None):
        self.requestedMessage = requestedMessage
        if connectorId:
            self.connectorId = connectorId

    def get_value(self):
        result = {
            "requestedMessage" : self.requestedMessage.get_value(),
        }
        if self.connectorId:
            result['connectorId'] = self.connectorId
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['requestedMessage'] = MessageTrigger.get_sample(option=option)
        if option:
            result['connectorId'] = 1
        return result