value 
decimal
1..1
Required. Indicates the measured value.
context
ReadingContextEnumType
0..1
Optional. Type of detail value: start, end or sample. Default = "Sample.Periodic"
measurand
MeasurandEnumType
0..1
Optional. Type of measurement. Default = "Energy.Active.Import.Register"
phase
PhaseEnumType
0..1
Optional. Indicates how the measured value is to be interpreted. For instance between L1 and neutral (L1-N) Please note that not all values of phase are applicable to all Measurands. When phase is absent, the measured value is interpreted as an overall value.
location
LocationEnumType
0..1
Optional. Indicates where the measured value has been sampled. Default = "Outlet"
signedMeterValue
SignedMeterValueType
0..1
Optional. Contains the MeterValueSignature with sign/encoding method information.
unitOfMeasure
UnitOfMeasureType
0..1
Optional. Represents a UnitOfMeasure including a multiplier