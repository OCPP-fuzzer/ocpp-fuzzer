ype
AttributeEnumType
0..1
Optional. Attribute: Actual, MinSet, MaxSet, etc. Defaults to Actual if absent.
value
string[0..2500]
0..1
Optional. Value of the attribute. May only be omitted when mutability is set to 'WriteOnly'.
mutability
MutabilityEnumType
0..1
Optional. Defines the mutability of this attribute. Default is ReadWrite when omitted.
persistent
boolean
0..1
Optional. If true, value will be persistent across system reboots or power down. Default when omitted is false.
constant
boolean
0..1
Optional. If true, value that will never be changed by the Charging Station at runtime. Default when omitted is false.