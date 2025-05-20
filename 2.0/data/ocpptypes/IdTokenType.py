idToken
identifierString[0..36]
1..1
Required. IdToken is case insensitive. Might hold the hidden id of an RFID tag, but can for example also contain a UUID.
type 
IdTokenEnumType
1..1
Required. Enumeration of possible idToken types.
additionalInfo
AdditionalInfoType
0..*
Optional. AdditionalInfo can be used to send extra information which can be validated by the CSMS in addition to the regular authorization with IdToken. AdditionalInfo contains one or more custom types, which need to be agreed upon by all parties involved. When AdditionalInfo is NOT implemented or a not supported AdditionalInfo.type is used, the CSMS/Charging Station MAY ignore the AdditionalInfo.