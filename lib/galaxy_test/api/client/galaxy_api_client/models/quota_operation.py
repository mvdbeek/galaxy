from enum import Enum, unique

__all__ = ["QuotaOperation"]


@unique
class QuotaOperation(str, Enum):
    """
    QuotaOperation Enum

    Args:
        = (str)                  : Value for MEMBER_EMPTY_STRING
        + (str)                  : Value for MEMBER_EMPTY_STRING_1
        - (str)                  : Value for _
    """

    MEMBER_EMPTY_STRING = "="
    MEMBER_EMPTY_STRING_1 = "+"
    _ = "-"
