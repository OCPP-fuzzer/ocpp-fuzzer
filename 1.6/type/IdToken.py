from type.CiString20Type import CiString20Type
    
class IdToken(CiString20Type):
    def get_value(self):
        return self

    @classmethod
    def get_members(cls):
        return [m for m in cls]
    