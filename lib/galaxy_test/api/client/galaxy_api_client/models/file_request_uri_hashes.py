from typing import TypeAlias

from .file_hash import FileHash

__all__ = ["FileRequestUriHashes"]

FileRequestUriHashes: TypeAlias = list[FileHash] | None
