evseId
integer
0..1
Optional. Specifies the id of the EVSE for which to clear charging profiles. An evseId of zero (0) specifies the charging profile for the overall Charging Station. Absence of this parameter means the clearing applies to all charging profiles that match the other criteria in the request.
chargingProfilePurpose
ChargingProfilePurposeEnumType
0..1
Optional. Specifies to purpose of the charging profiles that will be cleared, if they meet the other criteria in the request.
stackLevel
integer
0..1
Optional. Specifies the stackLevel for which charging profiles will be cleared, if they meet the other criteria in the request.