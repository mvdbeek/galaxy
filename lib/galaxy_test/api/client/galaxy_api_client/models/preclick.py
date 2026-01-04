from typing import TypeAlias

from .anonymous_array_item_64 import AnonymousArrayItem64

__all__ = ["Preclick"]

Preclick: TypeAlias = list[AnonymousArrayItem64] | bool | None
"""Alias for Elements that receive a click() event before the step is shown"""
