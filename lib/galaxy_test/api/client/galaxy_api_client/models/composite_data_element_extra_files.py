from typing import TypeAlias

from .extra_files import ExtraFiles

__all__ = ["CompositeDataElementExtraFiles"]

CompositeDataElementExtraFiles: TypeAlias = ExtraFiles | None
