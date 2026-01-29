from dataclasses import dataclass

from .tool_data_details_fields import ToolDataDetailsFields

__all__ = ["ToolDataDetails"]


@dataclass
class ToolDataDetails:
    """
    ToolDataDetails dataclass

    Args:
        columns (List[str])      : A list of column names
        model_class (str)        : The name of class modelling this tool data
        name (str)               : The name of this tool data entry
        fields (ToolDataDetailsFields | None)
                                 :
    """

    columns: list[str]  # A list of column names
    model_class: str  # The name of class modelling this tool data
    name: str  # The name of this tool data entry
    fields: ToolDataDetailsFields | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "columns": "columns",
            "fields": "fields",
            "model_class": "model_class",
            "name": "name",
        }
        key_transform_with_dump = {
            "columns": "columns",
            "fields": "fields",
            "model_class": "model_class",
            "name": "name",
        }
