from dataclasses import dataclass

__all__ = ["ToolDataEntry"]


@dataclass
class ToolDataEntry:
    """
    ToolDataEntry dataclass.

    Args:
        model_class (str)        : The name of class modelling this tool data
        name (str)               : The name of this tool data entry
    """

    model_class: str  # The name of class modelling this tool data
    name: str  # The name of this tool data entry
