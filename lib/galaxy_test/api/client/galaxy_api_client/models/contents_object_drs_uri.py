from typing import TypeAlias

__all__ = ["ContentsObjectDrsUri"]

ContentsObjectDrsUri: TypeAlias = list[str] | None
"""Alias for A list of full DRS identifier URI paths that may be used to obtain the object. These URIs may be external to this DRS instance."""
