from dataclasses import dataclass

from .escape_character import EscapeCharacter
from .quote_character import QuoteCharacter

__all__ = ["CsvDialect"]


@dataclass
class CsvDialect:
    """
    CsvDialect dataclass.

    Args:
        delimiter (str)          :
        double_quote (bool)      :
        escape_character (Optional[EscapeCharacter])
                                 :
        line_terminator (str)    :
        quote_character (Optional[QuoteCharacter])
                                 :
        skip_initial_space (bool):
    """

    delimiter: str
    double_quote: bool
    escape_character: EscapeCharacter | None
    line_terminator: str
    quote_character: QuoteCharacter | None
    skip_initial_space: bool
