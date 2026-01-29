from dataclasses import dataclass

from .parsed_column import ParsedColumn

__all__ = ["InferredColumnMapping"]


@dataclass
class InferredColumnMapping:
    """
    InferredColumnMapping dataclass.

    Args:
        column_index (int)       :
        column_title (str)       :
        parsed_column (ParsedColumn)
                                 :
    """

    column_index: int
    column_title: str
    parsed_column: ParsedColumn
