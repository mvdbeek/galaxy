from typing import TypeAlias

from .xref_dict import XrefDict

__all__ = ["UserToolSourceInputXrefs"]

UserToolSourceInputXrefs: TypeAlias = list[XrefDict] | None
