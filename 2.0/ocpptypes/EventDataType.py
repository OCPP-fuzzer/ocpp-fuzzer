from typing import Optional

from datetime import datetime

from ocppenum.EventTriggerEnumType import EventTriggerEnumType
from ocppenum.EventNotificationEnumType import EventNotificationEnumType
from ocpptypes.ComponentType import ComponentType
from ocpptypes.VariableType import VariableType

identifierString = str

class EventDataType:
    def __init__(self, eventId: int, timestamp: datetime, trigger: EventTriggerEnumType, actualValue: str, eventNotificationType: EventNotificationEnumType, component: ComponentType, variable: VariableType, cause: Optional[int] = None, techCode: Optional[str] = None, techInfo: Optional[str] = None, cleared: Optional[bool] = None, transactionId: Optional[identifierString] = None, variableMonitoringId: Optional[int] = None):
        self.eventId = eventId
        self.timestamp = timestamp
        self.trigger = trigger
        self.actualValue = actualValue
        self.eventNotificationType = eventNotificationType
        self.component = component
        self.variable = variable

        if cause:
            self.cause = cause
        if techCode:
            self.techCode = techCode
        if techInfo:
            self.techInfo = techInfo
        if cleared:
            self.cleared = cleared
        if transactionId:
            self.transactionId = transactionId
        if variableMonitoringId:
            self.variableMonitoringId = variableMonitoringId

    def to_dict(self):
        request = {
            "eventId" : self.eventId,
            "timestamp" : self.timestamp.isoformat().split('.')[0] + 'Z',
            "trigger" : self.trigger.value,
            "actualValue" : self.actualValue,
            "eventNotificationType" : self.eventNotificationType.value,
            "component" : self.component.to_dict(),
            "variable" : self.variable.to_dict(),
        }

        if self.cause:
            request["cause"] = self.cause
        if self.techCode:
            request["techCode"] = self.techCode
        if self.techInfo:
            request["techInfo"] = self.techInfo
        if self.cleared:
            request["cleared"] = self.cleared
        if self.transactionId:
            request["transactionId"] = self.transactionId
        if self.variableMonitoringId:
            request["variableMonitoringId"] = self.variableMonitoringId

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['eventId'] = 1
        result['timestamp'] = datetime.now().isoformat().split('.')[0] + 'Z'
        result['trigger'] = EventTriggerEnumType.sample()
        result['actualValue'] = "string"
        result['eventNotificationType'] = EventNotificationEnumType.sample()
        result['component'] = ComponentType.sample(option=option)
        result['variable'] = VariableType.sample(option=option)

        if option:
            result['cause'] = 1
            result['techCode'] = "string"
            result['techInfo'] = "string"
            result['cleared'] = True
            result['transactionId'] = str(__import__('uuid').uuid4())
            result['variableMonitoringId'] = 1

        return result
    