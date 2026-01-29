from typing import TypeAlias

from .anonymous_array_item_71 import AnonymousArrayItem71

__all__ = ["UserToolSourceOutputRequirements"]

UserToolSourceOutputRequirements: TypeAlias = list[AnonymousArrayItem71] | None
"""Alias for A list of requirements needed to execute this tool. These can be javascript expressions, resource requirements or container images."""
