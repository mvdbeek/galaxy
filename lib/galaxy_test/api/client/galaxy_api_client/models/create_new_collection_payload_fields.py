from typing import TypeAlias

from .field_dict import FieldDict

__all__ = ["CreateNewCollectionPayloadFields"]

CreateNewCollectionPayloadFields: TypeAlias = str | list[FieldDict] | None
"""Alias for List of fields to create for this collection. Set to 'auto' to guess fields from identifiers."""
