from typing import TypeAlias

from .list_jstree_response_item import ListJstreeResponseItem

__all__ = ["ListJstreeResponse"]

ListJstreeResponse: TypeAlias = list[ListJstreeResponseItem]
"""Alias for List of files in Jstree format."""
