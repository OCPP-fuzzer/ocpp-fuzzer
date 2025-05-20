Absolute
Schedule periods are relative to a fixed point in time defined in the schedule. This requires that startSchedule is set to a starting point in time.
Recurring
The schedule restarts periodically at the first schedule period. To be most useful, this requires that startSchedule is set to a starting point in time.
Relative
Charging schedule periods should start when the EVSE is ready to deliver energy. i.e. when the EV driver is authorized and the EV is connected. When a ChargingProfile is received for a transaction that is already charging, then the charging schedule periods should remain relative to the PowerPathClosed moment. No value for startSchedule should be supplied.