connectorId integer connectorId >= 0 1..1 Required. This contains a number (>0) designating a connector of the Charge Point.‘0’ (zero) is used to designate the main powermeter.
transactionId integer 0..1 Optional. The transaction to which these meter samples are related.
meterValue MeterValue 1..* Required. The sampled meter values with timestamps.