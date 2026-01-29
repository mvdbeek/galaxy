from typing import TypeAlias

__all__ = ["PathDataElementMd5"]

PathDataElementMd5: TypeAlias = str | None
"""Alias for The MD5 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the
integrity of the dataset. More information on MD5 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/MD5).
"""
