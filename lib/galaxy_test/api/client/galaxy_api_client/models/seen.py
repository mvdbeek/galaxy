from typing import TypeAlias

__all__ = ["Seen"]

Seen: TypeAlias = bool | None
"""Alias for Whether the notification should be marked as seen by the user. If not set, the notification will not be changed."""
