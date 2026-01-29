from typing import TypeAlias

from .position import Position

__all__ = ["ExtractUntypedParameterPosition"]

ExtractUntypedParameterPosition: TypeAlias = Position | None
