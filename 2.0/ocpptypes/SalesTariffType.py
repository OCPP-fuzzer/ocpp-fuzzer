from typing import Optional, List

from ocpptypes.SalesTariffEntryType import SalesTariffEntryType


class SalesTariffType:
    def __init__(self, id: int, salesTariffEntry: List[SalesTariffEntryType], salesTariffDescription: Optional[str] = None, numEPriceLevels: Optional[int] = None):
        self.id = id
        self.salesTariffEntry = salesTariffEntry

        if salesTariffDescription:
            self.salesTariffDescription = salesTariffDescription
        if numEPriceLevels:
            self.numEPriceLevels = numEPriceLevels

    def to_dict(self):
        request = {
            "id" : self.id,
            "salesTariffEntry" : [salesTariffEntry.to_dict() for salesTariffEntry in self.salesTariffEntry],
        }

        if self.salesTariffDescription:
            request["salesTariffDescription"] = self.salesTariffDescription
        if self.numEPriceLevels:
            request["numEPriceLevels"] = self.numEPriceLevels

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['id'] = 1
        result['salesTariffEntry'] = [SalesTariffEntryType.sample(option=option)]

        if option:
            result['salesTariffDescription'] = "string"
            result['numEPriceLevels'] = 1

        return result
    