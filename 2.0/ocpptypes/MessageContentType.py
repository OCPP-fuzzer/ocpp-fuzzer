from typing import Optional

from ocppenum.MessageFormatEnumType import MessageFormatEnumType


class MessageContentType:
    def __init__(self, format: MessageFormatEnumType, content: str, language: Optional[str] = None):
        self.format = format
        self.content = content

        if language:
            self.language = language

    def to_dict(self):
        request = {
            "format" : self.format.value,
            "content" : self.content,
        }

        if self.language:
            request["language"] = self.language

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['format'] = MessageFormatEnumType.sample()
        result['content'] = "string"

        if option:
            result['language'] = "string"

        return result
    