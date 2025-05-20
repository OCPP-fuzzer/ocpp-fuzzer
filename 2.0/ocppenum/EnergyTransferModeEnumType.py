from enum import Enum
    
class EnergyTransferModeEnumType(Enum):
    DC = "DC" 
    A_C_SINGLE_PHASE = "AC_single_phase" 
    A_C_TWO_PHASE = "AC_two_phase" 
    A_C_THREE_PHASE = "AC_three_phase" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    