from datetime import datetime
from typing import TypeAlias

__all__ = ["ServiceUpdatedAt"]

ServiceUpdatedAt: TypeAlias = datetime | None
"""Alias for Timestamp describing when the service was last updated (RFC 3339 format)"""
