evMaxCurrent
integer
1..1
Required. Maximum current (amps) supported by the electric vehicle. Includes cable capacity.
evMaxVoltage
integer
1..1
Required. Maximum voltage supported by the electric vehicle
energyAmount
integer
0..1
Optional. Amount of energy requested (in Wh). This inludes energy required for preconditioning.
evMaxPower
integer
0..1
Optional. Maximum power (in W) supported by the electric vehicle. Required for DC charging.
stateOfCharge
integer
0..1
Optional. Energy available in the battery (in percent of the battery capacity)
evEnergyCapacity
integer
0..1 
Optional. Capacity of the electric vehicle battery (in Wh)
fullSoC
integer
0..1
Optional. Percentage of SoC at which the EV considers the battery fully charged. (possible values: 0 - 100)
bulkSoC
integer
0..1
Optional. Percentage of SoC at which the EV considers a fast charging process to end. (possible values: 0 - 100)