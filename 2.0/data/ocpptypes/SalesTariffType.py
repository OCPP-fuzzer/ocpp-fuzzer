id
integer
1..1
Required. SalesTariff identifier used to identify one sales tariff. An SAID remains a unique identifier for one schedule throughout a charging session.
salesTariffDescription
string[0..32]
0..1
Optional. A human readable title/short description of the sales tariff e.g. for HMI display purposes.
numEPriceLevels
integer
0..1
Optional. Defines the overall number of distinct price levels used across all provided SalesTariff elements.
salesTariffEntry
SalesTariffEntryType
1..102 4
Required. Encapsulating element describing all relevant details for one time interval of the SalesTariff. The number of SalesTariffEntry elements is limited by the parameter maxScheduleTuples.