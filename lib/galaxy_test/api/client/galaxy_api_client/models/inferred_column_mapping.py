from dataclasses import dataclass

from .parsed_column import ParsedColumn

__all__ = ["InferredColumnMapping"]


@dataclass
class InferredColumnMapping:
    """
    InferredColumnMapping dataclass

    Args:
        column_index (int)       :
        column_title (str)       :
        parsed_column (ParsedColumn)
                                 :
    """

    column_index: int
    column_title: str
    parsed_column: ParsedColumn

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "column_index": "column_index",
            "column_title": "column_title",
            "parsed_column": "parsed_column",
        }
        key_transform_with_dump = {
            "column_index": "column_index",
            "column_title": "column_title",
            "parsed_column": "parsed_column",
        }
