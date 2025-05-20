ChargingStationExternalConstraints
Additional constraints that will be incorporated into a local power schedule. Only valid for a Charging Station. Therefore evse.Id MUST be 0 in the SetChargingProfileRequest message.
ChargingStationMaxProfile
Configuration for the maximum power or current available for an entire Charging Station.
TxDefaultProfile
Default profile that can be configured in the Charging Station. When a new transaction is started, this profile SHALL be used, unless it was a transaction that was started by a RequestStartTransactionRequest with a ChargingProfile that is accepted by the Charging Station.
TxProfile
Profile with constraints to be imposed by the Charging Station on the current transaction, or on a new transaction when this is started via a RequestStartTransactionRequest with a ChargingProfile. A profile with this purpose SHALL cease to be valid when the transaction terminates.