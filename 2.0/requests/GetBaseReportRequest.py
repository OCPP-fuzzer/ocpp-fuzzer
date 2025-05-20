from ocppenum.ReportBaseEnumType import ReportBaseEnumType


class GetBaseReportRequest:
    def __init__(self, requestId: int, reportBase: ReportBaseEnumType):
        self.requestId = requestId
        self.reportBase = reportBase

    def to_dict(self):
        request = {
            "requestId" : self.requestId,
            "reportBase" : self.reportBase.value,
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['requestId'] = 1
        result['reportBase'] = ReportBaseEnumType.sample()

        return result
    