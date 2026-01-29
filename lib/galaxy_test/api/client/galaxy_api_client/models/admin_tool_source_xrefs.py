from typing import TypeAlias

from .xref_dict import XrefDict

__all__ = ["AdminToolSourceXrefs"]

AdminToolSourceXrefs: TypeAlias = list[XrefDict] | None
