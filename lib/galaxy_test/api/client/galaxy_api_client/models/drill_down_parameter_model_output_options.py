from typing import TypeAlias

from .drill_down_options_dict_output import DrillDownOptionsDictOutput

__all__ = ["DrillDownParameterModelOutputOptions"]

DrillDownParameterModelOutputOptions: TypeAlias = list[DrillDownOptionsDictOutput] | None
