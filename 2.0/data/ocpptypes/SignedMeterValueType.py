signedMeterData
string[0..2500]
1..1
Required. Base64 encoded, contains the signed data which might contain more then just the meter value. It can contain information like timestamps, reference to a customer etc.
signingMethod
string[0..50]
1..1
Required. Method used to create the digital signature.
encodingMethod
string[0..50]
1..1
Required. Method used to encode the meter values before applying the digital signature algorithm.
publicKey
string[0..2500]
1..1
Required. Base64 encoded, sending depends on configuration variable PublicKeyWithSignedMeterValue.