from enum import Enum
    
class CostKindEnumType(Enum):
    CARBON_DIOXIDE_EMISSION = "CarbonDioxideEmission" 
    RELATIVE_PRICE_PERCENTAGE = "RelativePricePercentage" 
    RENEWABLE_GENERATION_PERCENTAGE = "RenewableGenerationPercentage" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    