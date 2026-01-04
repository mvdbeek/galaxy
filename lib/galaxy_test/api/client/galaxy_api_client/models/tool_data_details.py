from dataclasses import dataclass

from .columns import Columns
from .fields import Fields

__all__ = ["ToolDataDetails"]


@dataclass
class ToolDataDetails:
    """
    ToolDataDetails dataclass.

    Args:
        columns (Optional[Columns])
                                 : A list of column names
        model_class (str)        : The name of class modelling this tool data
        name (str)               : The name of this tool data entry
        fields (Optional[Fields]):
    """

    columns: Columns | None  # A list of column names
    model_class: str  # The name of class modelling this tool data
    name: str  # The name of this tool data entry
    fields: Fields | None = None
