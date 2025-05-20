costKind
CostKindEnumType
1..1
Required. The kind of cost referred to in the message element amount
amount 
integer
1..1
Required. The estimated or actual cost per kWh
amountMultiplier
integer
0..1
Optional. Values: -3..3, The amountMultiplier defines the exponent to base 10 (dec). The final value is determined by: amount * 10 ^ amountMultiplier