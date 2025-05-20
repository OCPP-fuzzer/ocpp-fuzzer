id
integer
1..1
Required. Unique id within an exchange context. It is defined within the OCPP context as a positive Integer value (greater or equal to zero).
priority
MessagePriorityEnumType
1..1
Required. With what priority should this message be shown
state
MessageStateEnumType
0..1
Optional. During what state should this message be shown. When omitted this message should be shown in any state of the Charging Station.
startDateTime
dateTime
0..1
Optional. From what date-time should this message be shown. If omitted: directly.
endDateTime
dateTime
0..1
Optional. Until what date-time should this message be shown, after this date/time this message SHALL be removed.
transactionId
identifierString[0..36]
0..1
Optional. During which transaction shall this message be shown. Message SHALL be removed by the Charging Station after transaction has ended.
message
MessageContentType
1..1
Required. Contains message details for the message to be displayed on a Charging Station.
display
ComponentType
0..1
Optional. When a Charging Station has multiple Displays, this field can be used to define to which Display this message belongs.