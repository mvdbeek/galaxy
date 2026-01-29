from typing import TypeAlias

__all__ = ["CreateNewCollectionPayloadFolderId"]

CreateNewCollectionPayloadFolderId: TypeAlias = str | None
"""Alias for The ID of the library folder that will contain the collection. Required if `instance_type=library`."""
