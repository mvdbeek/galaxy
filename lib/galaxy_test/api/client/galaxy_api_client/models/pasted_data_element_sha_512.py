from typing import TypeAlias

__all__ = ["PastedDataElementSha512"]

PastedDataElementSha512: TypeAlias = str | None
"""Alias for The SHA-512 checksum of the dataset. This is a hash of the dataset contents that can be used to verify the
integrity of the dataset. More information on SHA-512 checksums can be found on [Wikipedia](https://en.wikipedia.org/wiki/SHA-2).
"""
