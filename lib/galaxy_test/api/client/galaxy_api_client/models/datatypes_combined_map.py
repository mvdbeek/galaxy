from dataclasses import dataclass

from .datatypes import Datatypes
from .datatypes_map import DatatypesMap

__all__ = ["DatatypesCombinedMap"]


@dataclass
class DatatypesCombinedMap:
    """
    DatatypesCombinedMap dataclass.

    Args:
        datatypes (Datatypes)    : List of datatypes extensions
        datatypes_mapping (DatatypesMap)
                                 :
    """

    datatypes: Datatypes  # List of datatypes extensions
    datatypes_mapping: DatatypesMap
