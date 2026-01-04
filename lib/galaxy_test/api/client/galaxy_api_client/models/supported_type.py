from enum import Enum, unique

__all__ = ["SupportedType"]


@unique
class SupportedType(str, Enum):
    """
    SupportedType Enum

    Args:
        None (str)               : Value for NONE
        BasicAuth (str)          : Value for BASICAUTH
        BearerAuth (str)         : Value for BEARERAUTH
        PassportAuth (str)       : Value for PASSPORTAUTH
    """

    NONE = "None"
    BASICAUTH = "BasicAuth"
    BEARERAUTH = "BearerAuth"
    PASSPORTAUTH = "PassportAuth"
