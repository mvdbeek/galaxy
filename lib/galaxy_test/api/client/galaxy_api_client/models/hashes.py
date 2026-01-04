from typing import TypeAlias

from .file_hash import FileHash

__all__ = ["Hashes"]

Hashes: TypeAlias = list[FileHash] | None
"""Alias for List of precomputed hashes for the file, if available."""
