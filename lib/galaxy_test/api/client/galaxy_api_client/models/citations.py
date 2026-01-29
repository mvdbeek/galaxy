from typing import TypeAlias

from .citation import Citation

__all__ = ["Citations"]

Citations: TypeAlias = list[Citation] | None
