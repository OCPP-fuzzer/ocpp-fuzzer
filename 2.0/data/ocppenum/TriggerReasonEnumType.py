Authorized
Charging is authorized, by any means. Might be an RFID, or other authorization means.
CablePluggedIn
Cable is plugged in and EVDetected.
ChargingRateChanged
Rate of charging changed by more than LimitChangeSignificance.
ChargingStateChanged
Charging State changed.
Deauthorized
The transaction was stopped because of the authorization status in the response to a transactionEventRequest.
EnergyLimitReached
Maximum energy of charging reached. For example: in a pre-paid charging solution
EVCommunicationLost
Communication with EV lost, for example: cable disconnected.
EVConnectTimeout
EV not connected before the connection is timed out.
MeterValueClock
Needed to send a clock aligned meter value
MeterValuePeriodic
Needed to send a periodic meter value
TimeLimitReached
Maximum time of charging reached. For example: in a pre-paid charging solution
Trigger
Requested by the CSMS via a TriggerMessageRequest.
UnlockCommand
CSMS sent an Unlock Connector command.
StopAuthorized
An EV Driver has been authorized to stop charging. For example: By swiping an RFID card.
EVDeparted
EV departed. For example: When a departing EV triggers a parking bay detector.
EVDetected
EV detected. For example: When an arriving EV triggers a parking bay detector.
RemoteStop
A RequestStopTransactionRequest has been sent.
RemoteStart
A RequestStartTransactionRequest has been sent.
AbnormalCondition
An Abnormal Error or Fault Condition has occurred.
SignedDataReceived
Signed data is received from the energy meter.
ResetCommand
CSMS sent a Reset Charging Station command.