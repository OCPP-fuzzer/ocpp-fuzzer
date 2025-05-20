location
string[0..512]
1..1
Required. This contains a string containing a URI pointing to a location from which to retrieve the firmware.
retries
integer
0..1
Optional. This specifies how many times the Charging Station must retry to download the firmware before giving up. If this field is not present, it is left to Charging Station to decide how many times it wants to retry. If the value is 0, it means: no retries.
checksum
identifierString[0..32]
1..1
Required. The MD5 checksum over the entire firmware file as a hexadecimal string of length 32.
retryInterval
integer
0..1
Optional. The interval in seconds after which a retry may be attempted. If this field is not present, it is left to Charging Station to decide how long to wait between attempts.