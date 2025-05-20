connectorId integer 1..1 Required. The ID of the Connector for which the schedule is requested. When ConnectorId=0, the Charge Point will calculate the expected consumption for the grid connection.
duration integer 1..1 Required. Time in seconds. length of requested schedule
chargingRateUnit ChargingRateUnitType 0..1 Optional. Can be used to force a power or current profile