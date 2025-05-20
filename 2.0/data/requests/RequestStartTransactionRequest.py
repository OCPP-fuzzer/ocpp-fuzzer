evseId
integer
0..1
Optional. Number of the EVSE on which to start the transaction. EvseId SHALL be > 0
remoteStartId
integer
1..1
Required. Id given by the server to this start request. The Charging Station will return this in the TransactionEventRequest, letting the server know which transaction was started for this request.
idToken
IdTokenType
1..1
Required. The identifier that the Charging Station must use to start a transaction.
chargingProfile
ChargingProfileType
0..1
Optional. Charging Profile to be used by the Charging Station for the requested transaction. ChargingProfilePurpose MUST be set to TxProfile
groupIdToken
IdTokenType
0..1
Optional. The groupIdToken is only relevant when the transaction is to be started on an EVSE for which a reservation for groupIdToken is active, and the configuration variable AuthorizeRemoteStart = false (otherwise the AuthorizeResponse could return the groupIdToken).