attributeType
AttributeEnumType
0..1
Optional. Type of attribute: Actual, Target, MinSet, MaxSet. Default is Actual when omitted.
attributeValue
string[0..1000]
1..1
Required. Value to be assigned to attribute of variable.The value is allowed to be an empty string (""). The Configuration Variable ConfigurationValueSize can be used to limit SetVariableData.attributeValue and VariableCharacteristics.valueList. The max size of these values will always remain equal.
component
ComponentType
1..1
Required. The component for which the variable data is set.
variable 
VariableType
1..1 
Required. Specifies the that needs to be set.