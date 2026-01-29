from typing import TypeAlias

from .extra_files import ExtraFiles

__all__ = ["NestedElementExtraFiles"]

NestedElementExtraFiles: TypeAlias = ExtraFiles | None
