attributeStatus 
GetVariableStatusEnumType
1..1
Required. Result status of getting the variable.
attributeType
AttributeEnumType
0..1
Optional. Attribute type for which value is requested. When absent, default Actual is assumed.
attributeValue
string[0..2500]
0..1
Optional. Value of requested attribute type of component- variable. This field can only be empty when the givenstatus is NOT accepted.
component
ComponentType
1..1
Required. Component for which the Variable is requested.
variable
VariableType
1..1
Required. Variable for which the attribute value is requested.
attributeStatusInfo
StatusInfoType
0..1
Optional. Detailed attribute status information.