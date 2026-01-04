from typing import TypeAlias

from .composite_file_info import CompositeFileInfo

__all__ = ["CompositeFiles"]

CompositeFiles: TypeAlias = list[CompositeFileInfo] | None
"""Alias for A collection of files composing this data type"""
