requestId
integer
1..1
Required. Reference identification that is to be used by the Charging Station in the ReportChargingProfilesRequest when provided.
evseId
integer
0..1
Optional. For which EVSE installed charging profiles SHALL be reported. If 0, only charging profiles installed on the Charging Station itself (the grid connection) SHALL be reported. If omitted, all installed charging profiles SHALL be reported. Reported charging profiles SHALL match the criteria in field chargingProfile.
chargingProfile
ChargingProfileCriterionType
1..1
Required. Specifies the charging profile.