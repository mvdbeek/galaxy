from typing import TypeAlias

from .collection_element_identifier import CollectionElementIdentifier

__all__ = ["ElementIdentifiers"]

ElementIdentifiers: TypeAlias = list[CollectionElementIdentifier] | None
"""Alias for List of elements that should be in the new collection."""
