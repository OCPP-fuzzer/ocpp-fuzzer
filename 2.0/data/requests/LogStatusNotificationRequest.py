status
UploadLogStatusEnumType
1..1
Required. This contains the status of the log upload.
requestId
integer
0..1
Optional. The request id that was provided in GetLogRequest that started this log upload. This field is mandatory, unless the message was triggered by a TriggerMessageRequest AND there is no log upload ongoing.