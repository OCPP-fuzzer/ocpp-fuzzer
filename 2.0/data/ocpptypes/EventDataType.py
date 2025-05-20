eventId
integer
1..1
Required. Identifies the event. This field can be referred to as a cause by other events.
timestamp
dateTime
1..1
Required. Timestamp of the moment the report was generated.
trigger
EventTriggerEnumType
1..1
Required. Type of trigger for this event, e.g. exceeding a threshold value.
cause
integer
0..1
Optional. Refers to the Id of an event that is considered to be the cause for this event.
actualValue
string[0..2500]
1..1
Required. Actual value (attributeType Actual) of the variable. The Configuration Variable ReportingValueSize can be used to limit GetVariableResult.attributeValue, VariableAttribute.value and EventData.actualValue. The max size of these values will always remain equal.
techCode
string[0..50]
0..1
Optional. Technical (error) code as reported by component.
techInfo
string[0..500]
0..1
Optional. Technical detail information as reported by component.
cleared
boolean
0..1
Optional. Cleared is set to true to report the clearing of a monitored situation, i.e. a 'return to normal'.
transactionId
identifierString[0..36]
0..1
Optional. If an event notification is linked to a specific transaction, this field can be used to specify its transactionId.
variableMonitoringId
integer
0..1
Optional. Identifies the VariableMonitoring which triggered the event.
eventNotificationType
EventNotificationEnumType
1..1
Required. Specifies the event notification type of the message.
component
ComponentType
1..1
Required. Component for which event is notified.
variable
VariableType
1..1
Required. Variable for which event is notified.