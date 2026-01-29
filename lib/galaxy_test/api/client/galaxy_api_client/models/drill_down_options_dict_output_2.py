from dataclasses import dataclass

from .drill_down_options_dict_output import DrillDownOptionsDictOutput
from .drill_down_options_dict_output_name import DrillDownOptionsDictOutputName

__all__ = ["DrillDownOptionsDictOutput2"]


@dataclass
class DrillDownOptionsDictOutput2:
    """
    DrillDownOptionsDictOutput2 dataclass

    Args:
        name (DrillDownOptionsDictOutputName)
                                 :
        options (List[DrillDownOptionsDictOutput])
                                 :
        selected (bool)          :
        value (str)              :
    """

    name: DrillDownOptionsDictOutputName
    options: list[DrillDownOptionsDictOutput]
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
