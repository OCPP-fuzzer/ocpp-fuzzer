startPeriod
integer
1..1
Required. Start of the period, in seconds from the start of schedule. The value of StartPeriod also defines the stop time of the previous period.
limit
decimal
1..1
Required. Charging rate limit during the schedule period, in the applicable chargingRateUnit, for example in Amperes (A) or Watts (W). Accepts at most one digit fraction (e.g. 8.1).
numberPhases
integer
0..1
Optional. The number of phases that can be used for charging.For a DC EVSE this field should be omitted.For an AC EVSE a default value of numberPhases = 3 will be assumed if the field is absent.
phaseToUse
integer
0..1
Optional. Values: 1..3, Used if numberPhases=1 and if the EVSE is capable of switching the phase connected to the EV, i.e. ACPhaseSwitchingSupported is defined and true. It’s not allowed unless both conditions above are true. If both conditions are true, and phaseToUse is omitted, the Charging Station / EVSE will make the selection on its own.