id
integer
0..1
Optional. An id SHALL only be given to replace an existing monitor. The Charging Station handles the generation of id’s for new monitors.
transaction
boolean
0..1
Optional. Monitor only active when a transaction is ongoing on a component relevant to this transaction. Default = false.
value
decimal
1..1
Required. Value for threshold or delta monitoring. For Periodic or PeriodicClockAligned this is the interval in seconds.
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
Required. Component for which monitor is set.
variable
VariableType
1..1
Required. Variable for which monitor is set.