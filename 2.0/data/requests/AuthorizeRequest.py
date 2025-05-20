certificate
string[0..5500]
0..1 
Optional. The X.509 certificate chain presented by EV and encoded in PEM format. Order of certificates in chain is from leaf up to (but excluding) root certificate. Only needed in case of central contract validation when Charging Station cannot validate the contract certificate.
idToken
IdTokenType
1..1
Required. This contains the identifier that needs to be authorized.
iso15118CertificateHashData
OCSPRequestDataType
0..4
Optional. Contains the information needed to verify the EV Contract Certificate via OCSP. Not needed if certificate is provided.