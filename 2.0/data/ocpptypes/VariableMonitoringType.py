id 
integer 
1..1 
Required. Identifies the monitor.
transaction
boolean
1..1
Required. Monitor only active when a transaction is ongoing on a component relevant to this transaction.
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
Required. The severity that will be assigned to an event that is triggered by this monitor. The severity range is 0-9,with 0 as the highest and 9 as the lowest severity level.