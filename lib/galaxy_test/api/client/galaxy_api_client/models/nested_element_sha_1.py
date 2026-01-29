from typing import TypeAlias

__all__ = ["NestedElementSha1"]

NestedElementSha1: TypeAlias = str | None
"""Alias for The SHA1 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the
integrity of the dataset. More information on SHA1 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/SHA-1).
"""
