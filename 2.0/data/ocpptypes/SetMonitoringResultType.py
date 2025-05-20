id
integer
0..1
Optional. Id given to the VariableMonitor by the Charging Station. The Id is only returned when status is accepted. Installed VariableMonitors should have unique id’s but the id’s of removed Installed monitors should have unique id’s but the id’s of removed monitors MAY be reused.
status
SetMonitoringStatusEnumType
1..1
Required. Status is OK if a value could be returned. Otherwise this will indicate the reason why a value could not be returned.
type
MonitorEnumType
1..1
Required. The type of this monitor, e.g. a threshold, delta or periodic monitor.
severity
integer
1..1
Required. The severity that will be assigned to an event that is triggered by this monitor. The severity range is 0-9,
component
ComponentType
1..1
Required. Component for which status is returned.
variable
VariableType
1..1
Required. Variable for which status is returned.
statusInfo
StatusInfoType
0..1
Optional. Detailed status information.