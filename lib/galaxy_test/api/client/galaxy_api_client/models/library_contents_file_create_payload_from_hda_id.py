from typing import TypeAlias

__all__ = ["LibraryContentsFileCreatePayloadFromHdaId"]

LibraryContentsFileCreatePayloadFromHdaId: TypeAlias = str | None
"""Alias for (only if create_type is 'file') the encoded id of an accessible HDA to copy into the library"""
