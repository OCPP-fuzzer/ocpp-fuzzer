requestId
integer
1..1
Required. Id used to match the GetChargingProfilesRequest message with the resulting ReportChargingProfilesRequest messages. When the CSMS provided a requestId in the GetChargingProfilesRequest, this field SHALL contain the same value.
chargingLimitSource 
ChargingLimitSourceEnumType 
1..1 
Required. Source that has installed this charging profile.
tbc
boolean
0..1
Optional. To Be Continued. Default value when omitted: false. false indicates that there are no further messages as part of this report.
evseId
integer
1..1
Required. The evse to which the charging profile applies. If evseId = 0, the message contains an overall limit for the Charging Station.
chargingProfile
ChargingProfileType
1..*
Required. The charging profile as configured in the Charging Station.