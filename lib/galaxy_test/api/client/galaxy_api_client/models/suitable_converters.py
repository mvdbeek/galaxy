from typing import TypeAlias

from .suitable_converter import SuitableConverter

__all__ = ["SuitableConverters"]

SuitableConverters: TypeAlias = list[SuitableConverter]
"""Alias for Collection of converters that can be used on a particular dataset collection."""
