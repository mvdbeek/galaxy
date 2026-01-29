from dataclasses import dataclass

from .drill_down_options_dict_input_2 import DrillDownOptionsDictInput2
from .name import Name

__all__ = ["DrillDownOptionsDictInput3"]


@dataclass
class DrillDownOptionsDictInput3:
    """
    DrillDownOptionsDictInput3 dataclass.

    Args:
        name (Optional[Name])    : The name of the creator.
        options (List[DrillDownOptionsDictInput2])
                                 :
        selected (bool)          :
        value (str)              :
    """

    name: Name | None  # The name of the creator.
    options: list[DrillDownOptionsDictInput2]
    selected: bool
    value: str
