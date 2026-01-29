from typing import TypeAlias

from .anonymous_array_item_99 import AnonymousArrayItem99

__all__ = ["JobMessages"]

JobMessages: TypeAlias = list[AnonymousArrayItem99] | None
"""Alias for List with additional information and possible reasons for a failed job."""
