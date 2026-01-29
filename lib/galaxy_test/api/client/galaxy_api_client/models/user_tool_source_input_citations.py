from typing import TypeAlias

from .citation import Citation

__all__ = ["UserToolSourceInputCitations"]

UserToolSourceInputCitations: TypeAlias = list[Citation] | None
