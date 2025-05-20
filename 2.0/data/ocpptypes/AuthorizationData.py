idTokenInfo
IdTokenInfoType
0..1
Optional. Required when UpdateType is Full. This contains information about authorization status, expiry and group id. For a Differential update the following applies: If this element is present, then this entry SHALL be added or updated in the Local Authorization List. If this element is absent, the entry for this IdToken in the Local Authorization List SHALL be deleted.
idToken
IdTokenType
1..1
Required. This contains the identifier which needs to be stored for authorization.