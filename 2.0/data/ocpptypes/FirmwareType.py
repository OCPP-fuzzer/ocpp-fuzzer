location
string[0..512]
1..1
Required. URI defining the origin of the firmware.
retrieveDateTime
dateTime
1..1
Required. Date and time at which the firmware shall be retrieved.
installDateTime
dateTime
0..1
Optional. Date and time at which the firmware shall be installed.
signingCertificate
string[0..5500]
0..1
Optional. Certificate with which the firmware was signed. PEM encoded X.509 certificate.
signature
string
0..1
Optional. Base64 encoded firmware signature.