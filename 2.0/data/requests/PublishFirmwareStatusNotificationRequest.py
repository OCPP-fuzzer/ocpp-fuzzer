status
PublishFirmwareStatusEnumType
1..1
Required. This contains the progress status of the publishfirmware installation.
location
string[0..512]
0..*
Optional. Required if status is Published. Can be multiple URI’s, if the Local Controller supports e.g. HTTP, HTTPS, and FTP.
requestId
integer
0..1
Optional. The request id that was provided in the PublishFirmwareRequest which triggered this action.