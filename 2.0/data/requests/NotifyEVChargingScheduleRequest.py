timeBase
dateTime
1..1
Required. Periods contained in the charging profile are relative to this point in time.
evseId
integer
1..1
Required. The charging schedule contained in this notification applies to an EVSE. EvseId must be > 0.
chargingSchedule
ChargingScheduleType
1..1
Required. Planned energy consumption of the EV over time. Always relative to timeBase.