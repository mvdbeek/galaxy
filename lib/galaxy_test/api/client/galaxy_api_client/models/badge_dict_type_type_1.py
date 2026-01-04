from enum import Enum


class BadgeDictTypeType1(str, Enum):
    CLOUD = "cloud"
    NO_QUOTA = "no_quota"
    QUOTA = "quota"
    RESTRICTED = "restricted"
    USER_DEFINED = "user_defined"

    def __str__(self) -> str:
        return str(self.value)
