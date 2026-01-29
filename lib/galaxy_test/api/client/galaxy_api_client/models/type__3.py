from enum import Enum, unique

__all__ = ["Type3"]


@unique
class Type3(str, Enum):
    """
    Type3 Enum

    Args:
        string (str)             : Value for STRING
        int (str)                : Value for INT
        float (str)              : Value for FLOAT
        boolean (str)            : Value for BOOLEAN
        element_identifier (str) : Value for ELEMENT_IDENTIFIER
    """

    STRING = "string"
    INT = "int"
    FLOAT = "float"
    BOOLEAN = "boolean"
    ELEMENT_IDENTIFIER = "element_identifier"
