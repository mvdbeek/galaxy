from typing import TypeAlias

from .drill_down_options_dict_input import DrillDownOptionsDictInput

__all__ = ["DrillDownParameterModelInputOptions"]

DrillDownParameterModelInputOptions: TypeAlias = list[DrillDownOptionsDictInput] | None
