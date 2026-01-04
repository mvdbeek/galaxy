from enum import Enum, unique

__all__ = ["Status"]


@unique
class Status(str, Enum):
    """
    'ok' or 'error'

    Args:
        ok (str)                 : Value for OK
        error (str)              : Value for ERROR
    """

    OK = "ok"
    ERROR = "error"
