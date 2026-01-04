from enum import Enum, unique

__all__ = ["DefaultQuotaValues"]


@unique
class DefaultQuotaValues(str, Enum):
    """
    DefaultQuotaValues Enum

    Args:
        unregistered (str)       : Value for UNREGISTERED
        registered (str)         : Value for REGISTERED
        no (str)                 : Value for NO
    """

    UNREGISTERED = "unregistered"
    REGISTERED = "registered"
    NO = "no"
