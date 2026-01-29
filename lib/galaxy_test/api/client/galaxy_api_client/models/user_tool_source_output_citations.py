from typing import TypeAlias

from .citation import Citation

__all__ = ["UserToolSourceOutputCitations"]

UserToolSourceOutputCitations: TypeAlias = list[Citation] | None
