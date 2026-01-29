from enum import Enum, unique

__all__ = ["AnonymousArrayItem54TypeEnum"]


@unique
class AnonymousArrayItem54TypeEnum(str, Enum):
    """
    Discriminator enum for AnonymousArrayItem54 union types.

    Args:
        regex (str)              : Value for REGEX
        in_range (str)           : Value for IN_RANGE
        length (str)             : Value for LENGTH
    """

    REGEX = "regex"
    IN_RANGE = "in_range"
    LENGTH = "length"
