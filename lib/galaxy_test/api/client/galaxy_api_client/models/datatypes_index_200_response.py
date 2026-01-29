from typing import TypeAlias

from .datatype_details import DatatypeDetails

__all__ = ["DatatypesIndex200Response"]

DatatypesIndex200Response: TypeAlias = list[DatatypeDetails] | list[str]
