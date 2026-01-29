from typing import TypeAlias

__all__ = ["LibraryContentsFileCreatePayloadFromHdcaId"]

LibraryContentsFileCreatePayloadFromHdcaId: TypeAlias = str | None
"""Alias for (only if create_type is 'file') the encoded id of an accessible HDCA to copy into the library"""
