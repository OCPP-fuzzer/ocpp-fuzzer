
class ClearDisplayMessageRequest:
    def __init__(self, id: int):
        self.id = id

    def to_dict(self):
        request = {
            "id" : self.id,
        }
        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['id'] = 1

        return result
    