id
integer
1..1
Required. Id of ChargingProfile.
stackLevel
integer
1..1
Required. Value determining level in hierarchy stack of profiles. Higher values have precedence over lower values. Lowest level is 0.
chargingProfilePurpose
ChargingProfilePurposeEnumType
1..1
Required. Defines the purpose of the schedule transferred by this profile
chargingProfileKind
ChargingProfileKindEnumType
1..1
Required. Indicates the kind of schedule.
recurrencyKind
RecurrencyKindEnumType
0..1
Optional. Indicates the start point of a recurrence.
validFrom
dateTime
0..1
Optional. Point in time at which the profile starts to be valid. If absent, the profile is valid as soon as it is received by the Charging Station.
validTo
dateTime
0..1
Optional. Point in time at which the profile stops to be valid. If absent, the profile is valid until it is replaced by another profile.
transactionId
identifierString[0..36]
0..1
Optional. SHALL only be included when ChargingProfilePurpose is set to TxProfile in a SetChargingProfileRequest. The transactionId is used to match the profile to a specific transaction.
chargingSchedule
ChargingScheduleType
1..3
Required. Schedule that contains limits for the available power or current over time. In order to support ISO 15118 schedule negotiation, it supports at most three schedules with associated tariff to choose from. Having multiple chargingSchedules is only allowed for charging profiles of purpose TxProfile in the context of an ISO 15118 charging session.