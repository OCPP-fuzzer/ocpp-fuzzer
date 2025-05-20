requestId
integer
1..1
Required. The id of the GetMonitoringRequest that requested this report.
tbc
boolean
0..1
Optional. “to be continued” indicator. Indicates whether another part of the monitoringData follows in an upcoming notifyMonitoringReportRequest message. Default value when omitted is false.
seqNo
integer
1..1
Required. Sequence number of this message. First message starts at 0.
generatedAt
dateTime
1..1
Required. Timestamp of the moment this message was generated at the Charging Station.
monitor
MonitoringDataType
0..*
Optional. List of MonitoringData containing monitoring settings.