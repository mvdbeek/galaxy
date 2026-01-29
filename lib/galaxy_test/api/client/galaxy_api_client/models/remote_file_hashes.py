from typing import TypeAlias

from .remote_file_hash import RemoteFileHash

__all__ = ["RemoteFileHashes"]

RemoteFileHashes: TypeAlias = list[RemoteFileHash] | None
"""Alias for List of precomputed hashes for the file, if available."""
