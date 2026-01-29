from enum import Enum, unique

__all__ = ["InvocationSerializationView"]


@unique
class InvocationSerializationView(str, Enum):
    """
    InvocationSerializationView Enum

    Args:
        element (str)            : Value for ELEMENT
        collection (str)         : Value for COLLECTION
    """

    ELEMENT = "element"
    COLLECTION = "collection"
