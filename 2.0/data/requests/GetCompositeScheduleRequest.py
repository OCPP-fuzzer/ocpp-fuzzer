duration
integer
1..1
Required. Length of the requested schedule in seconds.
chargingRateUnit
ChargingRateUnitEnumType
0..1
Optional. Can be used to force a power or current profile.
evseId
integer
1..1
Required. The ID of the EVSE for which the schedule is requested. When evseId=0, the Charging Station will calculate the expected consumption for the grid connection.