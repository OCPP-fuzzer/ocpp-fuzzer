idTag IdToken 0..1 Optional. This contains the identifier which requested to stop the charging. It is optional because a Charge Point may terminate charging without the presence of an idTag, e.g. in case of a reset. A Charge Point SHALL send the idTag if known.
meterStop integer 1..1 Required. This contains the meter value in Wh for the connector at end of the transaction.
timestamp dateTime 1..1 Required. This contains the date and time on which the transaction is stopped.
transactionId integer 1..1 Required. This contains the transaction-id as received by the StartTransaction.conf.
reason Reason 0..1 Optional. This contains the reason why the transaction was stopped. MAY only be omitted when the Reason is "Local".
transactionData MeterValue 0..* Optional. This contains transaction usage details relevant for billing purposes.