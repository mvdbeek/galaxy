from dataclasses import dataclass
from datetime import datetime

from .ids import Ids

__all__ = ["XrefItem"]


@dataclass
class XrefItem:
    """
    XrefItem dataclass.

    Args:
        access_time (datetime)   : Date and time the external reference was accessed
        ids (Ids)                : List of reference identifiers
        name (str)               : Name of external reference
        namespace (str)          : External resource vendor prefix
    """

    access_time: datetime  # Date and time the external reference was accessed
    ids: Ids  # List of reference identifiers
    name: str  # Name of external reference
    namespace: str  # External resource vendor prefix
