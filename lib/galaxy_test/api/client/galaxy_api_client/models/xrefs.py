from typing import TypeAlias

from .xref_dict import XrefDict

__all__ = ["Xrefs"]

Xrefs: TypeAlias = list[XrefDict] | None
