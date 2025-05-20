from enum import Enum
    
class ConnectorEnumType(Enum):
    CCCS1 = "cCCS1" 
    CCCS2 = "cCCS2" 
    CG105 = "cG105" 
    CTESLA = "cTesla" 
    CTYPE1 = "cType1" 
    CTYPE2 = "cType2" 
    ## S309-1P-16A = "s309-1P-16A" 
    ## S309-1P-32A = "s309-1P-32A" 
    ## S309-3P-16A = "s309-3P-16A" 
    ## S309-3P-32A = "s309-3P-32A" 
    SBS1361 = "sBS1361" 
    ## SCEE-7-7 = "sCEE-7-7" 
    STYPE2 = "sType2" 
    STYPE3 = "sType3" 
    OTHER1_PH_MAX16_A = "Other1PhMax16A" 
    OTHER1_PH_OVER16_A = "Other1PhOver16A" 
    OTHER3_PH = "Other3Ph" 
    PAN = "Pan" 
    WINDUCTIVE = "wInductive" 
    WRESONANT = "wResonant" 
    UNDETERMINED = "Undetermined" 
    UNKNOWN = "Unknown" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    