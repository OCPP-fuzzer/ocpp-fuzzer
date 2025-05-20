UpperThreshold
Triggers an event notice when the actual value of the Variable rises above monitorValue
LowerThreshold
Triggers an event notice when the actual value of the Variable drops below monitorValue.
Delta
Triggers an event notice when the actual value has changed more than plus or minus monitorValue since the time that this monitor was set or since the last time this event notice was sent, whichever was last. For variables that are not numeric, like boolean, string or enumerations, a monitor of type Delta will trigger an event notice whenever the variable changes, regardless of the value of monitorValue.
Periodic
Triggers an event notice every monitorValue seconds interval, starting from the time that this monitor was set.
PeriodicClockAligned
Triggers an event notice every monitorValue seconds interval, starting from the nearest clock-aligned interval after this monitor was set. For example, a monitorValue of 900 will trigger event notices at 0, 15, 30 and 45 minutes after the hour, every hour.