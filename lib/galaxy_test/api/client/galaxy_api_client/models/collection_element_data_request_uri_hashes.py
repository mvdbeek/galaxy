from typing import TypeAlias

from .file_hash import FileHash

__all__ = ["CollectionElementDataRequestUriHashes"]

CollectionElementDataRequestUriHashes: TypeAlias = list[FileHash] | None
