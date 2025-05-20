chargingProfilePurpose
ChargingProfilePurposeEnumType
0..1
Optional. Defines the purpose of the schedule transferred by this profile
stackLevel
integer
0..1
Optional. Value determining level in hierarchy stack of profiles. Higher values have precedence over lower values. Lowest level is 0.
chargingProfileId
integer
0..*
Optional. List of all the chargingProfileIds requested. Any ChargingProfile that matches one of these profiles will be reported. If omitted, the Charging Station SHALL not filter on chargingProfileId. This field SHALL NOT contain more ids than set in ChargingProfileEntries.maxLimit
chargingLimitSource
ChargingLimitSourceEnumType
0..4
Optional. For which charging limit sources, charging profiles SHALL be reported. If omitted, the Charging Station SHALL not filter on chargingLimitSource.