from typing import TypeAlias

from .anonymous_array_item_2 import AnonymousArrayItem2

__all__ = ["Headers"]

Headers: TypeAlias = list[AnonymousArrayItem2] | None
"""Alias for An optional list of headers to include in the HTTP request to `url`. These headers can be used to provide auth tokens required to fetch the object bytes."""
