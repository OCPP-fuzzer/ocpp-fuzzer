value String 1..1 Required. Value as a “Raw” (decimal) number or “SignedData”. Field Type is “string” to allow for digitally signed data readings. Decimal numeric values are also acceptable to allow fractional values for measurands such as Temperature and Current.
context ReadingContext 0..1 Optional. Type of detail value: start, end or sample. Default = “Sample.Periodic”
format ValueFormat 0..1 Optional. Raw or signed data. Default = “Raw”
measurand Measurand 0..1 Optional. Type of measurement. Default = “Energy.Active.Import.Register”
phase Phase 0..1 Optional. indicates how the measured value is to be interpreted. For instance between L1 and neutral (L1-N) Please note that not all values of phase are applicable to all Measurands. When phase is absent, the measured value is interpreted as an overall value.
location Location 0..1 Optional. Location of measurement. Default=”Outlet”
unit UnitOfMeasure 0..1 Optional. Unit of the value. Default = “Wh” if the (default) measurand is an “Energy” type.