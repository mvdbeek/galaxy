from datetime import datetime
from typing import TypeAlias

__all__ = ["HdaInaccessibleUpdateTime"]

HdaInaccessibleUpdateTime: TypeAlias = datetime | None
"""Alias for The last time and date this item was updated."""
