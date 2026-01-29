from enum import Enum, unique

__all__ = ["BadgeDictSource"]


@unique
class BadgeDictSource(str, Enum):
    """
    BadgeDictSource Enum

    Args:
        admin (str)              : Value for ADMIN
        galaxy (str)             : Value for GALAXY
    """

    ADMIN = "admin"
    GALAXY = "galaxy"
