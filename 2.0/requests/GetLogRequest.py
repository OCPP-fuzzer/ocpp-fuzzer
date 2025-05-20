from typing import Optional

from ocppenum.LogEnumType import LogEnumType
from ocpptypes.LogParametersType import LogParametersType


class GetLogRequest:
    def __init__(self, logType: LogEnumType, requestId: int, log: LogParametersType, retries: Optional[int] = None, retryInterval: Optional[int] = None):
        self.logType = logType
        self.requestId = requestId
        self.log = log

        if retries:
            self.retries = retries
        if retryInterval:
            self.retryInterval = retryInterval

    def to_dict(self):
        request = {
            "logType" : self.logType.value,
            "requestId" : self.requestId,
            "log" : self.log.to_dict(),
        }

        if self.retries:
            request["retries"] = self.retries
        if self.retryInterval:
            request["retryInterval"] = self.retryInterval

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['logType'] = LogEnumType.sample()
        result['requestId'] = 1
        result['log'] = LogParametersType.sample(option=option)

        if option:
            result['retries'] = 1
            result['retryInterval'] = 1

        return result
    