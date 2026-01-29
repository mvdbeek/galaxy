from typing import TypeAlias

from .extra_files import ExtraFiles

__all__ = ["ServerDirElementExtraFiles"]

ServerDirElementExtraFiles: TypeAlias = ExtraFiles | None
