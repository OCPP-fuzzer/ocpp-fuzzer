data
string[0..512]
1..1
Required. (Part of) the requested data. No format specified in which the data is returned. Should be human readable.
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
requestId 
integer 
1..1
Required. The Id of the request.