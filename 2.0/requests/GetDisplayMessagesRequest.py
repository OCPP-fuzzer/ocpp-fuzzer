from typing import List, Optional

from ocppenum.MessagePriorityEnumType import MessagePriorityEnumType
from ocppenum.MessageStateEnumType import MessageStateEnumType


class GetDisplayMessagesRequest:
    def __init__(self, requestId: int, id: Optional[List[int]] = None, priority: Optional[MessagePriorityEnumType] = None, state: Optional[MessageStateEnumType] = None):
        self.requestId = requestId

        if id:
            self.id = id
        if priority:
            self.priority = priority
        if state:
            self.state = state

    def to_dict(self):
        request = {
            "requestId" : self.requestId,
        }

        if self.id:
            request["id"] = [id for id in self.id]
        if self.priority:
            request["priority"] = self.priority.value
        if self.state:
            request["state"] = self.state.value

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['requestId'] = 1

        if option:
            result['id'] = [1]
            result['priority'] = MessagePriorityEnumType.sample()
            result['state'] = MessageStateEnumType.sample()

        return result
    