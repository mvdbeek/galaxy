from typing import TypeAlias

from .anonymous_array_item_62 import AnonymousArrayItem62

__all__ = ["Postclick"]

Postclick: TypeAlias = list[AnonymousArrayItem62] | bool | None
"""Alias for Elements that receive a click() event after the step is shown"""
