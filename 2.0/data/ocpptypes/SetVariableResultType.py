attributeType
AttributeEnumType
0..1
Optional. Type of attribute: Actual, Target, MinSet, MaxSet. Default is Actual when omitted.
attributeStatus
SetVariableStatusEnumType
1..1
Required. Result status of setting the variable.
component
ComponentType
1..1
Required. The component for which result is returned.
variable
VariableType
1..1
Required. The variable for which the result is returned.
attributeStatusInfo
StatusInfoType
0..1
Optional. Detailed attribute status information.