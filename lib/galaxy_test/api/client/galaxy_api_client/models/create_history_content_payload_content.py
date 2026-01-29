from typing import TypeAlias

__all__ = ["CreateHistoryContentPayloadContent"]

CreateHistoryContentPayloadContent: TypeAlias = str | None
"""Alias for Depending on the `source` it can be:
- The encoded id from the library dataset
- The encoded id from the library folder
- The encoded id from the HDA
- The encoded id from the HDCA
"""
