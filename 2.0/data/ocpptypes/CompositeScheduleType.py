evseId
integer
1..1
Required. The ID of the EVSE for which the schedule is requested. When evseid=0, the Charging Station calculated the expected consumption for the grid connection.
duration
integer
1..1
Required. Duration of the schedule in seconds.
scheduleStart
dateTime
1..1
Required. Date and time at which the schedule becomes active. All time measurements within the schedule are relative to this timestamp.
chargingRateUnit
ChargingRateUnitEnumType
1..1
Required. The unit of measure Limit is expressed in.
chargingSchedulePeriod
ChargingSchedulePeriodType
1..*
Required. List of ChargingSchedulePeriod elements defining maximum power or current usage over time.