from typing import TypeAlias

from .supported_type import SupportedType

__all__ = ["AuthorizationsSupportedTypes"]

AuthorizationsSupportedTypes: TypeAlias = list[SupportedType] | None
"""Alias for An Optional list of support authorization types. More than one can be supported and tried in sequence. Defaults to `None` if empty or missing."""
