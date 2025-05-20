class CiString500Type(str):

    MAX_LENGTH = 500

    def __new__(cls, value):
        if not isinstance(value, str):
            raise TypeError("LimitedStr only accepts string values.")

        if len(value) > cls.MAX_LENGTH:
            raise ValueError(f"String exceeds maximum length of {cls.MAX_LENGTH} characters.")

        return super().__new__(cls, value)

    @classmethod
    def get_sample(cls, option=False):
        min_len = 1
        max_len = cls.MAX_LENGTH
        random = __import__("random")
        string = __import__("string")

        length = random.randint(min_len, max_len)
        chars = string.ascii_letters + string.digits
        return ''.join(random.choices(chars, k=length))
    