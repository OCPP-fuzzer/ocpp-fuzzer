connectorId integer connectorId >= 0 1..1 Required. The id of the connector for which the status is reported. Id '0' (zero) is used if the status is for the Charge Point main controller.
errorCode ChargePointErrorCode 1..1 Required. This contains the error code reported by the Charge Point.
info CiString50Type 0..1 Optional. Additional free format information related to the error.
status ChargePointStatus 1..1 Required. This contains the current status of the Charge Point.
timestamp dateTime 0..1 Optional. The time for which the status is reported. If absent time of receipt of the message will be assumed.
vendorId CiString255Type 0..1 Optional. This identifies the vendor-specific implementation.
vendorErrorCode CiString50Type 0..1 Optional. This contains the vendor-specific error code.