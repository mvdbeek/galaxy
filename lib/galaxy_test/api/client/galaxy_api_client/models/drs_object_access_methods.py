from typing import TypeAlias

from .access_method import AccessMethod

__all__ = ["DrsObjectAccessMethods"]

DrsObjectAccessMethods: TypeAlias = list[AccessMethod] | None
"""Alias for The list of access methods that can be used to fetch the `DrsObject`.
Required for single blobs; optional for bundles."""
