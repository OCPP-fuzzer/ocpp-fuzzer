logType
LogEnumType
1..1
Required. This contains the type of log file that the Charging Station should send.
requestId
integer
1..1
Required. The Id of this request.
retries
integer
0..1
Optional. This specifies how many times the Charging Station must retry to upload the log before giving up. If this field is not present, it is left to Charging Station to decide how many times it wants to retry. If the value is 0, it means: no retries.
retryInterval
integer
0..1
Optional. The interval in seconds after which a retry may be attempted. If this field is not present, it is left to Charging Station to decide how long to wait between attempts.
log
LogParametersType
1..1
Required. This field specifies the requested log and the location to which the log should be sent.