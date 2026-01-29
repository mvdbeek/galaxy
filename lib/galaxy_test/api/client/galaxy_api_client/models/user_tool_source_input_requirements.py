from typing import TypeAlias

from .anonymous_array_item_48 import AnonymousArrayItem48

__all__ = ["UserToolSourceInputRequirements"]

UserToolSourceInputRequirements: TypeAlias = list[AnonymousArrayItem48] | None
"""Alias for A list of requirements needed to execute this tool. These can be javascript expressions, resource requirements or container images."""
