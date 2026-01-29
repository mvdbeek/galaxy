from typing import TypeAlias

from .group_response import GroupResponse

__all__ = ["GroupListResponse"]

GroupListResponse: TypeAlias = list[GroupResponse]
"""Alias for Response schema for listing groups."""
