status
AuthorizationStatusEnumType
1..1
Required. Current status of the ID Token.
cacheExpiryDateTime
dateTime
0..1
Optional. Date and Time after which the token must be considered invalid.
chargingPriority
integer
0..1
Optional. Priority from a business point of view. Default priority is 0, The range is from -9 to 9. Higher values indicate a higher priority. The chargingPriority in TransactionEventResponse overrules this one.
language1
string[0..8]
0..1
Optional. Preferred user interface language of identifier user. Contains a language code as defined in [RFC5646].
evseId
integer
0..*
Optional. Only used when the IdToken is only valid for one or more specific EVSEs, not for the entire Charging Station.
language2
string[0..8]
0..1
Optional. Second preferred user interface language of identifier user. Don’t use when language1 is omitted, has to be different from language1. Contains a language code as defined in [RFC5646].
groupIdToken
IdTokenType
0..1 
Optional. This contains the group identifier.
personalMessage
MessageContentType
0..1
Optional. Personal message that can be shown to the EV Driver and can be used for tariff information, user greetings etc.