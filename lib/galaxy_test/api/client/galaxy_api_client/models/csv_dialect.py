from dataclasses import dataclass

from .csv_dialect_escape_character import CsvDialectEscapeCharacter
from .csv_dialect_quote_character import CsvDialectQuoteCharacter

__all__ = ["CsvDialect"]


@dataclass
class CsvDialect:
    """
    CsvDialect dataclass

    Args:
        delimiter (str)          :
        double_quote (bool)      :
        escape_character (CsvDialectEscapeCharacter)
                                 :
        line_terminator (str)    :
        quote_character (CsvDialectQuoteCharacter)
                                 :
        skip_initial_space (bool):
    """

    delimiter: str
    double_quote: bool
    escape_character: CsvDialectEscapeCharacter
    line_terminator: str
    quote_character: CsvDialectQuoteCharacter
    skip_initial_space: bool

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "delimiter": "delimiter",
            "double_quote": "double_quote",
            "escape_character": "escape_character",
            "line_terminator": "line_terminator",
            "quote_character": "quote_character",
            "skip_initial_space": "skip_initial_space",
        }
        key_transform_with_dump = {
            "delimiter": "delimiter",
            "double_quote": "double_quote",
            "escape_character": "escape_character",
            "line_terminator": "line_terminator",
            "quote_character": "quote_character",
            "skip_initial_space": "skip_initial_space",
        }
