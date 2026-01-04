from dataclasses import dataclass

from .parse_log import ParseLog
from .parsed_column import ParsedColumn
from .rows import Rows

__all__ = ["ParsedWorkbook"]


@dataclass
class ParsedWorkbook:
    """
    ParsedWorkbook dataclass.

    Args:
        extra_columns (List[ParsedColumn])
                                 :
        parse_log (ParseLog)     :
        rows (Optional[Rows])    : Specify rows of metadata data corresponding to an
                                   identifier if collection_type is sample_sheet
    """

    extra_columns: list[ParsedColumn]
    parse_log: ParseLog
    rows: Rows | None  # Specify rows of metadata data corresponding to an identifier if collection_type is sample_sheet
