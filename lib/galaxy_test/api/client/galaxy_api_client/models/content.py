from typing import TypeAlias

__all__ = ["Content"]

Content: TypeAlias = str | None
"""Alias for Text contents of the last page revision with embedded directives expanded (type dependent on content_format)."""
