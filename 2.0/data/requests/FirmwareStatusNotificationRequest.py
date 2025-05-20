status
FirmwareStatusEnumType
1..1
Required. This contains the progress status of the firmware installation.
requestId
integer
0..1
Optional. The request id that was provided in the UpdateFirmwareRequest that started this firmware update. This field is mandatory, unless the message was triggered by a TriggerMessageRequest AND there is no firmware update ongoing.