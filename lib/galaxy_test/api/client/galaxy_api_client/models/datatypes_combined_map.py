from dataclasses import dataclass

from .datatypes_map import DatatypesMap

__all__ = ["DatatypesCombinedMap"]


@dataclass
class DatatypesCombinedMap:
    """
    DatatypesCombinedMap dataclass

    Args:
        datatypes (List[str])    : List of datatypes extensions
        datatypes_mapping (DatatypesMap)
                                 :
    """

    datatypes: list[str]  # List of datatypes extensions
    datatypes_mapping: DatatypesMap

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "datatypes": "datatypes",
            "datatypes_mapping": "datatypes_mapping",
        }
        key_transform_with_dump = {
            "datatypes": "datatypes",
            "datatypes_mapping": "datatypes_mapping",
        }
