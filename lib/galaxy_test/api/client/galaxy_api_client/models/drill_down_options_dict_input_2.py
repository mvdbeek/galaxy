from dataclasses import dataclass

from .drill_down_options_dict_input import DrillDownOptionsDictInput
from .drill_down_options_dict_input_name import DrillDownOptionsDictInputName

__all__ = ["DrillDownOptionsDictInput2"]


@dataclass
class DrillDownOptionsDictInput2:
    """
    DrillDownOptionsDictInput2 dataclass

    Args:
        name (DrillDownOptionsDictInputName)
                                 :
        options (List[DrillDownOptionsDictInput])
                                 :
        selected (bool)          :
        value (str)              :
    """

    name: DrillDownOptionsDictInputName
    options: list[DrillDownOptionsDictInput]
    selected: bool
    value: str

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "name": "name",
            "options": "options",
            "selected": "selected",
            "value": "value",
        }
        key_transform_with_dump = {
            "name": "name",
            "options": "options",
            "selected": "selected",
            "value": "value",
        }
