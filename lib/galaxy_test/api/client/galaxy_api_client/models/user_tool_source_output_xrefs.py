from typing import TypeAlias

from .xref_dict import XrefDict

__all__ = ["UserToolSourceOutputXrefs"]

UserToolSourceOutputXrefs: TypeAlias = list[XrefDict] | None
