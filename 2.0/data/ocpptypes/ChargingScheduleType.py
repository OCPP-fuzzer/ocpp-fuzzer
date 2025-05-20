id 
integer
1..1
Required. Identifies the ChargingSchedule.
startSchedule
dateTime
0..1
Optional. Starting point of an absolute or recurring schedule.
duration
integer
0..1
Optional. Duration of the charging schedule in seconds. If the duration is left empty, the last period will continue indefinitely or until end of the transaction if chargingProfilePurpose = TxProfile.
chargingRateUnit 
ChargingRateUnitEnumType
1..1
Required. The unit of measure Limit is expressed in.
minChargingRate
decimal
0..1
Optional. Minimum charging rate supported by the EV. The unit of measure is defined by the chargingRateUnit. This parameter is intended to be used by a local smart charging algorithm to optimize the power allocation for in the case a charging process is inefficient at lower charging rates. Accepts at most one digit fraction (e.g. 8.1)
chargingSchedulePeriod
ChargingSchedulePeriodType
1..1024
Required. List of ChargingSchedulePeriod elements defining maximum power or current usage over time. The maximum number of periods, that is supported by the Charging Station, if less than 1024, is set by device model variable SmartChargingCtrlr.PeriodsPerSchedule.
salesTariff
SalesTariffType
0..1
Optional. Sales tariff associated with this charging schedule.