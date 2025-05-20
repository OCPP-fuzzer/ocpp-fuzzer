eventType
TransactionEventEnumType
1..1
Required. This contains the type of this event. The first TransactionEvent of a transaction SHALL contain: "Started" The last TransactionEvent of a transaction SHALL contain: "Ended" All others SHALL contain: "Updated"
timestamp
dateTime
1..1
Required. The date and time at which this transaction event occurred.
triggerReason
TriggerReasonEnumType
1..1
Required. Reason the Charging Station sends this message to the CSMS
seqNo
integer
1..1
Required. Incremental sequence number, helps with determining if all messages of a transaction have been received.
offline
boolean
0..1
Optional. Indication that this transaction event happened when the Charging Station was offline. Default = false, meaning: the event occurred when the Charging Station was online.
numberOfPhasesUsed
integer
0..1
Optional. If the Charging Station is able to report the number of phases used, then it SHALL provide it. When omitted the CSMS may be able to determine the number of phases used via device management.
cableMaxCurrent
integer
0..1
Optional. The maximum current of the connected cable in Ampere (A).
reservationId
integer
0..1
Optional. This contains the Id of the reservation that terminates as a result of this transaction.transactionInfo TransactionType 1..1 Required. Contains transaction specific information.
transactionInfo 
TransactionType 
1..1 
Required. Contains transaction specific information.
idToken
IdTokenType
0..1
Optional. This contains the identifier for which a transaction is (or will be) started or stopped. Is required when the EV Driver becomes authorized for this transaction and when the EV Driver ends authorization. The IdToken should only be sent once in a TransactionEventRequest for every authorization (for starting or for stopping) done for this transaction, so that CSMS can return the idTokenInfo in the TransactionEventResponse. idToken should not be present in the TransactionEventRequest when a transaction is ended by a RequestStopTransactionRequest or a ResetRequest.
evse
EVSEType
0..1
Optional. This identifies which evse (and connector) of the Charging Station is used.
meterValue
MeterValueType
0..*
Optional. This contains the relevant meter values. Depending on the EventType of this TransactionEvent the following Configuration Variable is used to configure thecontent:Started: SampledDataTxStartedMeasurandsUpdated: SampledDataTxUpdatedMeasurands Ended: SampledDataTxEndedMeasurands & AlignedDataTxEndedMeasurands