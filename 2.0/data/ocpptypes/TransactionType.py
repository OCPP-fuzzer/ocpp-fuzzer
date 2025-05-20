transactionId 
identifierString[0..36]
1..1
Required. This contains the Id of the transaction.
chargingState
ChargingStateEnumType
0..1
Optional. Current charging state, is required when state has changed.
timeSpentCharging
integer
0..1
Optional. Contains the total time that energy flowed from EVSE to EV during the transaction (in seconds). Note that timeSpentCharging is smaller or equal to the duration of the transaction.
stoppedReason
ReasonEnumType
0..1
Optional. The <i>stoppedReason </i>is the reason/event that initiated the process of stopping the transaction. It will normally be the user stopping authorization via card (Local or MasterPass) or app (Remote), but it can also be CSMS revoking authorization (DeAuthorized), or disconnecting the EV when TxStopPoint = EVConnected (EVDisconnected). Most other reasons are related to technical faults or energy limitations. MAY only be omitted when <i>stoppedReason </i>is "Local"
remoteStartId
integer
0..1
Optional. The ID given to remote start request (RequestStartTransactionRequest. This enables to CSMS to match the started transaction to the given start request.