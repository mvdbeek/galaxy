from enum import Enum, unique

__all__ = ["PluginAspectStatusState"]


@unique
class PluginAspectStatusState(str, Enum):
    """
    PluginAspectStatusState Enum

    Args:
        ok (str)                 : Value for OK
        not_ok (str)             : Value for NOT_OK
        unknown (str)            : Value for UNKNOWN
    """

    OK = "ok"
    NOT_OK = "not_ok"
    UNKNOWN = "unknown"
