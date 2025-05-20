chargingProfileId integer 1..1 Required. Unique identifier for this profile.
transactionId integer 0..1 Optional. Only valid if ChargingProfilePurpose is set to TxProfile, the transactionId MAY be used to match the profile to a specific transaction.
stackLevel integer >=0 1..1 Required. Value determining level in hierarchy stack of profiles. Higher values have precedence over lower values. Lowest level is 0.
chargingProfilePurpose ChargingProfilePurposeType 1..1 Required. Defines the purpose of the schedule transferred by this message.
chargingProfileKind ChargingProfileKindType 1..1 Required. Indicates the kind of schedule.
recurrencyKind RecurrencyKindType 0..1 Optional. Indicates the start point of a recurrence.
validFrom dateTime 0..1 Optional. Point in time at which the profile starts to be valid. If absent, the profile is valid as soon as it is received by the Charge Point.
validTo dateTime 0..1 Optional. Point in time at which the profile stops to be valid. If absent, the profile is valid until it is replaced by another profile.
chargingSchedule ChargingSchedule 1..1 Required. Contains limits for the available power or current over time.