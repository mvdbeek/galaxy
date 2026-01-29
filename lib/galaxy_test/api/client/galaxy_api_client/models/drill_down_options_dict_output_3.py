from dataclasses import dataclass

from .drill_down_options_dict_output_2 import DrillDownOptionsDictOutput2
from .name import Name

__all__ = ["DrillDownOptionsDictOutput3"]


@dataclass
class DrillDownOptionsDictOutput3:
    """
    DrillDownOptionsDictOutput3 dataclass.

    Args:
        name (Optional[Name])    : The name of the creator.
        options (List[DrillDownOptionsDictOutput2])
                                 :
        selected (bool)          :
        value (str)              :
    """

    name: Name | None  # The name of the creator.
    options: list[DrillDownOptionsDictOutput2]
    selected: bool
    value: str
