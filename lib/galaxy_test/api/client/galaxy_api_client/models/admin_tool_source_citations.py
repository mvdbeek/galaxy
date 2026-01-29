from typing import TypeAlias

from .citation import Citation

__all__ = ["AdminToolSourceCitations"]

AdminToolSourceCitations: TypeAlias = list[Citation] | None
