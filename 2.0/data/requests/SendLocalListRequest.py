versionNumber
integer
1..1
Required. In case of a full update this is the version number of the full list. In case of a differential update it is the version number of the list after the update has been applied.
updateType
UpdateEnumType
1..1
Required. This contains the type of update (full or differential) of this request.
localAuthorizationList
AuthorizationData
0..*
Optional. This contains the Local Authorization List entries.