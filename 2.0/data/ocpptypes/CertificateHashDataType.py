hashAlgorithm 
HashAlgorithmEnumType
1..1
Required. Used algorithms for the hashes provided.
issuerNameHash
identifierString[0..128]
1..1
Required. The hash of the issuer’s distinguished name (DN), that must be calculated over the DER encoding of the issuer’s name field in the certificate being checked.
issuerKeyHash
string[0..128]
1..1
Required. The hash of the DER encoded public key: the value (excluding tag and length) of the subject public key field in the issuer’s certificate.
serialNumber
identifierString[0..40]
1..1
Required. The string representation of the hexadecimal value of the serial number without the prefix "0x" and without leading zeroes.