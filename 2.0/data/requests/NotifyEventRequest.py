generatedAt
dateTime
1..1
Required. Timestamp of the moment this message was generated at the Charging Station.
tbc
boolean
0..1
Optional. “to be continued” indicator. Indicates whether another part of the report follows in an upcoming notifyEventRequest message. Default value when omitted is false.
seqNo
integer
1..1
Required. Sequence number of this message. First message starts at 0.
eventData
EventDataType
1..*
Required. List of EventData. An EventData element contains only the Component, Variable and VariableMonitoring data that caused the event. The list of EventData will usally contain one eventData element, but the Charging Station may decide to group multiple events in one notification. For example, when multiple events triggered at the same time.