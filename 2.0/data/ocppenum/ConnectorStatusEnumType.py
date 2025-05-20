Available
When a Connector becomes available for a new User (Operative)
Occupied
When a Connector becomes occupied, so it is not available for a new EV driver. (Operative)
Reserved
When a Connector becomes reserved as a result of ReserveNow command (Operative)
Unavailable
When a Connector becomes unavailable as the result of a Change Availability command or an event upon which the Charging Station transitions to unavailable at its discretion. Upon receipt of ChangeAvailability message command, the status MAY change immediately or the change MAY be scheduled. When scheduled, StatusNotification SHALL be sent when the availability change becomes effective (Inoperative)
Faulted
When a Connector (or the EVSE or the entire Charging Station it belongs to) has reported an error and is not available for energy delivery. (Inoperative).