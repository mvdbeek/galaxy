from typing import TypeAlias

from .xref_item import XrefItem

__all__ = ["PrepareStoreDownloadPayloadBcoOverrideXref"]

PrepareStoreDownloadPayloadBcoOverrideXref: TypeAlias = list[XrefItem] | None
"""Alias for Override xref for 'description domain' when generating BioCompute object."""
