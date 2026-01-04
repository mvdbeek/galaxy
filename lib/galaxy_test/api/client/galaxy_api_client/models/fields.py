from typing import TypeAlias

from .field_dict import FieldDict

__all__ = ["Fields"]

Fields: TypeAlias = list[FieldDict] | str | None
