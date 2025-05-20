requestId
integer
1..1
Required. The Id of the request.
report
boolean
1..1
Required. Flag indicating whether the Charging Station should return NotifyCustomerInformationRequest messages containing information about the customer referred to.
clear
boolean
1..1
Required. Flag indicating whether the Charging Station should clear all information about the customer referred to.
customerIdentifier
string[0..64]
0..1
Optional. A (e.g. vendor specific) identifier of the customer this request refers to. This field contains a custom identifier other than IdToken and Certificate. One of the possible identifiers (customerIdentifier, customerIdToken or customerCertificate) should be in the request message.
idToken
IdTokenType
0..1
Optional. The IdToken of the customer this request refers to. One of the possible identifiers (customerIdentifier, customerIdToken or customerCertificate) should be in the request message.
customerCertificate
CertificateHashDataType
0..1
Optional. The Certificate of the customer this request refers to. One of the possible identifiers (customerIdentifier, customerIdToken or customerCertificate) should be in the request message.