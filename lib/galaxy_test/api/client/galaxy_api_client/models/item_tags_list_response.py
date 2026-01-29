from typing import TypeAlias

from .item_tags_response import ItemTagsResponse

__all__ = ["ItemTagsListResponse"]

ItemTagsListResponse: TypeAlias = list[ItemTagsResponse]
"""Alias for Response schema for listing item tags."""
