iso15118SchemaVersion
string[0..50]
1..1
Required. Schema version currently used for the 15118 session between EV and Charging Station. Needed for parsing of the EXI stream by the CSMS.
action
CertificateActionEnumType
1..1
Required. Defines whether certificate needs to be installed or updated.
exiRequest
string[0..5600]
1..1
Required. Raw CertificateInstallationReq request from EV, Base64 encoded.