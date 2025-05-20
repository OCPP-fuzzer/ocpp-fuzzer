unit
string[0..16]
0..1
Optional. Unit of the variable. When the transmitted value has a unit, this field SHALL be included.
dataType
DataEnumType
1..1
Required. Data type of this variable.
minLimit
decimal
0..1
Optional. Minimum possible value of this variable.
maxLimit
decimal
0..1
Optional. Maximum possible value of this variable. When the datatype of this Variable is String, OptionList, SequenceList or MemberList, this field defines the maximum length of the (CSV) string.
valuesList
string[0..1000]
0..1
Optional. Mandatory when dataType = OptionList, MemberList or SequenceList. valuesList specifies theallowed values for the type.
supportsMonitoring
boolean
1..1
Required. Flag indicating if this variable supports monitoring.