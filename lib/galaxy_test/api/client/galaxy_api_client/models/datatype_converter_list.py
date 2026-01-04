from typing import TypeAlias

from .datatype_converter import DatatypeConverter

__all__ = ["DatatypeConverterList"]

DatatypeConverterList: TypeAlias = list[DatatypeConverter]
