from enum import Enum, unique

__all__ = ["PluginKind"]


@unique
class PluginKind(str, Enum):
    """
    Enum to distinguish between different kinds or categories of plugins.

    Args:
        rfs (str)                : Value for RFS
        drs (str)                : Value for DRS
        rdm (str)                : Value for RDM
        stock (str)              : Value for STOCK
    """

    RFS = "rfs"
    DRS = "drs"
    RDM = "rdm"
    STOCK = "stock"
