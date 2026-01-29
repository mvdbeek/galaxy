from dataclasses import dataclass

from .parsed_column import ParsedColumn

__all__ = ["SplitUpPairedDataLogEntry"]


@dataclass
class SplitUpPairedDataLogEntry:
    """
    SplitUpPairedDataLogEntry dataclass.

    Args:
        message (str)            :
        new_paired_status_column (int)
                                 :
        old_forward_column (ParsedColumn)
                                 :
        old_reverse_column (ParsedColumn)
                                 :
    """

    message: str
    new_paired_status_column: int
    old_forward_column: ParsedColumn
    old_reverse_column: ParsedColumn
