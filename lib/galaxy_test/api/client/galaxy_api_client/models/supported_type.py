from enum import Enum


class SupportedType(str, Enum):
    BASICAUTH = "BasicAuth"
    BEARERAUTH = "BearerAuth"
    NONE = "None"
    PASSPORTAUTH = "PassportAuth"

    def __str__(self) -> str:
        return str(self.value)
