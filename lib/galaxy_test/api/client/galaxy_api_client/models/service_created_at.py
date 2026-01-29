from datetime import datetime
from typing import TypeAlias

__all__ = ["ServiceCreatedAt"]

ServiceCreatedAt: TypeAlias = datetime | None
"""Alias for Timestamp describing when the service was first deployed and available (RFC 3339 format)"""
