from typing import TypeAlias

from .label_value import LabelValue

__all__ = ["Options"]

Options: TypeAlias = list[LabelValue] | None
