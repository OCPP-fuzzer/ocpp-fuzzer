from enum import Enum
    
class InstallCertificateUseEnumType(Enum):
    V2_G_ROOT_CERTIFICATE = "V2GRootCertificate" 
    M_O_ROOT_CERTIFICATE = "MORootCertificate" 
    C_S_M_S_ROOT_CERTIFICATE = "CSMSRootCertificate" 
    MANUFACTURER_ROOT_CERTIFICATE = "ManufacturerRootCertificate" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    