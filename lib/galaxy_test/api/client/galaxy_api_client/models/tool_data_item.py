from dataclasses import dataclass

__all__ = ["ToolDataItem"]


@dataclass
class ToolDataItem:
    """
    ToolDataItem dataclass.

    Args:
        values (str)             : A `\t` (TAB) separated list of column __contents__. You
                                   must specify a value for each of the columns of the data
                                   table.
    """

    values: str  # A `\t` (TAB) separated list of column __contents__. You must specify a value for each of the columns of the data table.
