evseId
integer
0..1
Optional. The charging schedule contained in this notification applies to an EVSE. evseId must be > 0.
chargingLimit
ChargingLimitType
1..1
Required. This contains the source of the charging limit and whether it is grid critical.
chargingSchedule
ChargingScheduleType
0..*
Optional. Contains limits for the available power or current over time, as set by the external source.