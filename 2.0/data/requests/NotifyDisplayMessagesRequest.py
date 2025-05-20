requestId
integer
1..1
Required. The id of the GetDisplayMessagesRequest that requested this message.
tbc
boolean
0..1
Optional. "to be continued" indicator. Indicates whether another part of the report follows in an upcoming NotifyDisplayMessagesRequest message. Default value when omitted is false.
messageInfo
MessageInfoType
0..*
Optional. The requested display message as configured in the Charging Station.