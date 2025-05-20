connectorId integer 0..1 Optional. Number of the connector on which to start the transaction. connectorId SHALL be > 0
idTag IdToken 1..1 Required. The identifier that Charge Point must use to start a transaction.
chargingProfile ChargingProfile 0..1 Optional. Charging Profile to be used by the Charge Point for the requested transaction. ChargingProfilePurpose MUST be set to TxProfile