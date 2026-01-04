from datetime import datetime
from typing import TypeAlias

__all__ = ["UpdatedTime"]

UpdatedTime: TypeAlias = datetime | None
"""Alias for Timestamp of content update in RFC3339, identical to `created_time` in systems that do not support updates. (This is the update time of the underlying content, not of the JSON object.)"""
