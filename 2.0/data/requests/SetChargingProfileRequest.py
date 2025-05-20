evseId
integer
1..1
Required. For TxDefaultProfile an evseId=0 applies the profile to each individual evse. For ChargingStationMaxProfile and ChargingStationExternalConstraints an evseId=0 contains an overal limit for the whole Charging Station.
chargingProfile
ChargingProfileType
1..1
Required. The charging profile to be set at the Charging Station.