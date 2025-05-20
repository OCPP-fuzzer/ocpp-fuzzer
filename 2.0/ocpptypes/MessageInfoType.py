from typing import Optional

from datetime import datetime

from ocppenum.MessagePriorityEnumType import MessagePriorityEnumType
from ocppenum.MessageStateEnumType import MessageStateEnumType
from ocpptypes.MessageContentType import MessageContentType
from ocpptypes.ComponentType import ComponentType

identifierString = str

class MessageInfoType:
    def __init__(self, id: int, priority: MessagePriorityEnumType, message: MessageContentType, state: Optional[MessageStateEnumType] = None, startDateTime: Optional[datetime] = None, endDateTime: Optional[datetime] = None, transactionId: Optional[identifierString] = None, display: Optional[ComponentType] = None):
        self.id = id
        self.priority = priority
        self.message = message

        if state:
            self.state = state
        if startDateTime:
            self.startDateTime = startDateTime
        if endDateTime:
            self.endDateTime = endDateTime
        if transactionId:
            self.transactionId = transactionId
        if display:
            self.display = display

    def to_dict(self):
        request = {
            "id" : self.id,
            "priority" : self.priority.value,
            "message" : self.message.to_dict(),
        }

        if self.state:
            request["state"] = self.state.value
        if self.startDateTime:
            request["startDateTime"] = self.startDateTime.isoformat().split('.')[0] + 'Z'
        if self.endDateTime:
            request["endDateTime"] = self.endDateTime.isoformat().split('.')[0] + 'Z'
        if self.transactionId:
            request["transactionId"] = self.transactionId
        if self.display:
            request["display"] = self.display.to_dict()

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['id'] = 1
        result['priority'] = MessagePriorityEnumType.sample()
        result['message'] = MessageContentType.sample(option=option)

        if option:
            result['state'] = MessageStateEnumType.sample()
            result['startDateTime'] = datetime.now().isoformat().split('.')[0] + 'Z'
            result['endDateTime'] = datetime.now().isoformat().split('.')[0] + 'Z'
            result['transactionId'] = str(__import__('uuid').uuid4())
            result['display'] = ComponentType.sample(option=option)

        return result
    