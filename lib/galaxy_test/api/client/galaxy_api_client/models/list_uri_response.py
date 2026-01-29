from typing import TypeAlias

from .list_uri_response_item import ListUriResponseItem

__all__ = ["ListUriResponse"]

ListUriResponse: TypeAlias = list[ListUriResponseItem]
"""Alias for List of directories and files."""
