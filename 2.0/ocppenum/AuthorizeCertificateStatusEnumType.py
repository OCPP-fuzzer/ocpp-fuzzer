from enum import Enum
    
class AuthorizeCertificateStatusEnumType(Enum):
    ACCEPTED = "Accepted" 
    SIGNATURE_ERROR = "SignatureError" 
    CERTIFICATE_EXPIRED = "CertificateExpired" 
    CERTIFICATE_REVOKED = "CertificateRevoked" 
    NO_CERTIFICATE_AVAILABLE = "NoCertificateAvailable" 
    CERT_CHAIN_ERROR = "CertChainError" 
    CONTRACT_CANCELLED = "ContractCancelled" 

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    
    @classmethod
    def sample(cls):
        value = __import__('random').choice(list(cls))

        return value.value
    