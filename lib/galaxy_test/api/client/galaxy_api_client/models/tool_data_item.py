from dataclasses import dataclass

__all__ = ["ToolDataItem"]


@dataclass
class ToolDataItem:
    """
    ToolDataItem dataclass

    Args:
        values (str)             : A `\t` (TAB) separated list of column __contents__. You
                                   must specify a value for each of the columns of the data
                                   table.
    """

    values: str  # A `\t` (TAB) separated list of column __contents__. You must specify a value for each of the columns of the data table.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "values": "values",
        }
        key_transform_with_dump = {
            "values": "values",
        }
