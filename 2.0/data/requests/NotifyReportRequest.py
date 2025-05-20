requestId
integer
1..1
Required. The id of the GetReportRequest or GetBaseReportRequest that requested this report
generatedAt
dateTime
1..1
Required. Timestamp of the moment this message was generated at the Charging Station.
tbc
boolean
0..1
Optional. “to be continued” indicator. Indicates whether another part of the report follows in an upcoming notifyReportRequest message. Default value when omitted is false.
seqNo
integer
1..1
Required. Sequence number of this message. First message starts at 0.reportData ReportDataType 0..* Optional. List of ReportData.