from typing import TypeAlias

__all__ = ["ParentId"]

ParentId: TypeAlias = str | None
"""Alias for Encoded ID of the parent folder. Empty if it's the root folder."""
