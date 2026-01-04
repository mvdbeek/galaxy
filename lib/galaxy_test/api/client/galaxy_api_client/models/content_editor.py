from typing import TypeAlias

__all__ = ["ContentEditor"]

ContentEditor: TypeAlias = str | None
"""Alias for Raw text contents of the last page revision (type dependent on content_format)."""
