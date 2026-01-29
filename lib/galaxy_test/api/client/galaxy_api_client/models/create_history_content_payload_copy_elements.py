from typing import TypeAlias

__all__ = ["CreateHistoryContentPayloadCopyElements"]

CreateHistoryContentPayloadCopyElements: TypeAlias = bool | None
"""Alias for If the source is a collection, whether to copy child HDAs into the target history as well. Prior to the galaxy release 23.1 this defaulted to false."""
