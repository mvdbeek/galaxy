from typing import TypeAlias

__all__ = ["CollectionType"]

CollectionType: TypeAlias = str | None
"""Alias for The type of the collection, can be `list`, `paired`, or define subcollections using `:` as separator like `list:paired` or `list:list`."""
