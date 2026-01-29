from typing import TypeAlias

from .label_value import LabelValue

__all__ = ["SelectParameterModelOptions"]

SelectParameterModelOptions: TypeAlias = list[LabelValue] | None
