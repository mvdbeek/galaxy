from dataclasses import dataclass

from .parsed_column import ParsedColumn

__all__ = ["SplitUpPairedDataLogEntry"]


@dataclass
class SplitUpPairedDataLogEntry:
    """
    SplitUpPairedDataLogEntry dataclass

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

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "message": "message",
            "new_paired_status_column": "new_paired_status_column",
            "old_forward_column": "old_forward_column",
            "old_reverse_column": "old_reverse_column",
        }
        key_transform_with_dump = {
            "message": "message",
            "new_paired_status_column": "new_paired_status_column",
            "old_forward_column": "old_forward_column",
            "old_reverse_column": "old_reverse_column",
        }
