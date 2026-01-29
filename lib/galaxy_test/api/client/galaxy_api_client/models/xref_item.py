from dataclasses import dataclass
from datetime import datetime

__all__ = ["XrefItem"]


@dataclass
class XrefItem:
    """
    XrefItem dataclass

    Args:
        access_time (datetime)   : Date and time the external reference was accessed
        ids (List[str])          : List of reference identifiers
        name (str)               : Name of external reference
        namespace (str)          : External resource vendor prefix
    """

    access_time: datetime  # Date and time the external reference was accessed
    ids: list[str]  # List of reference identifiers
    name: str  # Name of external reference
    namespace: str  # External resource vendor prefix

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "access_time": "access_time",
            "ids": "ids",
            "name": "name",
            "namespace": "namespace",
        }
        key_transform_with_dump = {
            "access_time": "access_time",
            "ids": "ids",
            "name": "name",
            "namespace": "namespace",
        }
