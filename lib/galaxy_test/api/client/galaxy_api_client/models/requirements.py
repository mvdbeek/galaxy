from typing import TypeAlias

from .anonymous_array_item_19 import AnonymousArrayItem19

__all__ = ["Requirements"]

Requirements: TypeAlias = list[AnonymousArrayItem19] | None
"""Alias for A list of requirements needed to execute this tool. These can be javascript expressions, resource requirements or container images."""
