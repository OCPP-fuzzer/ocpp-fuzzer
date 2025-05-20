from datetime import datetime

from ocppenum.ConnectorStatusEnumType import ConnectorStatusEnumType


class StatusNotificationRequest:
    def __init__(self, timestamp: datetime, connectorStatus: ConnectorStatusEnumType, evseId: int, connectorId: int):
        self.timestamp = timestamp
        self.connectorStatus = connectorStatus
        self.evseId = evseId
        self.connectorId = connectorId

    def to_dict(self):
        request = {
            "timestamp" : self.timestamp.isoformat().split('.')[0] + 'Z',
            "connectorStatus" : self.connectorStatus.value,
            "evseId" : self.evseId,
            "connectorId" : self.connectorId,
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['timestamp'] = datetime.now().isoformat().split('.')[0] + 'Z'
        result['connectorStatus'] = ConnectorStatusEnumType.sample()
        result['evseId'] = 1
        result['connectorId'] = 1

        return result
    