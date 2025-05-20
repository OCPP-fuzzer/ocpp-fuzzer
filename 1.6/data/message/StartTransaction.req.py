connectorId integer connectorId > 0 1..1 Required. This identifies which connector of the Charge Point is used.
idTag IdToken 1..1 Required. This contains the identifier for which a transaction has to be started.
meterStart integer 1..1 Required. This contains the meter value in Wh for the connector at start of the transaction.
reservationId integer 0..1 Optional. This contains the id of the reservation that terminates as a result of this transaction.
timestamp dateTime 1..1 Required. This contains the date and time on which the transaction is started.