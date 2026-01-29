from enum import Enum, unique

__all__ = ["AdminToolSourceOutputsItemTypeEnum"]


@unique
class AdminToolSourceOutputsItemTypeEnum(str, Enum):
    """
    Discriminator enum for AdminToolSourceOutputsItem union types.

    Args:
        data (str)               : Value for DATA
        text (str)               : Value for TEXT
        integer (str)            : Value for INTEGER
        float (str)              : Value for FLOAT
        boolean (str)            : Value for BOOLEAN
    """

    DATA = "data"
    TEXT = "text"
    INTEGER = "integer"
    FLOAT = "float"
    BOOLEAN = "boolean"
