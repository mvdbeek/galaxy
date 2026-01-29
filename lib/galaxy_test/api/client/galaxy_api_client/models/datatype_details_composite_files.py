from typing import TypeAlias

from .composite_file_info import CompositeFileInfo

__all__ = ["DatatypeDetailsCompositeFiles"]

DatatypeDetailsCompositeFiles: TypeAlias = list[CompositeFileInfo] | None
"""Alias for A collection of files composing this data type"""
