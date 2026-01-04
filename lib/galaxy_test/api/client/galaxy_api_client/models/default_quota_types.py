from enum import Enum, unique

__all__ = ["DefaultQuotaTypes"]


@unique
class DefaultQuotaTypes(str, Enum):
    """
    DefaultQuotaTypes Enum

    Args:
        unregistered (str)       : Value for UNREGISTERED
        registered (str)         : Value for REGISTERED
    """

    UNREGISTERED = "unregistered"
    REGISTERED = "registered"
