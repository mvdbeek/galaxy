from dataclasses import dataclass

from .parse_log import ParseLog
from .parsed_column import ParsedColumn
from .parsed_workbook_element import ParsedWorkbookElement
from .rows import Rows

__all__ = ["ParsedWorkbookForCollection"]


@dataclass
class ParsedWorkbookForCollection:
    """
    ParsedWorkbookForCollection dataclass.

    Args:
        elements (List[ParsedWorkbookElement])
                                 :
        extra_columns (List[ParsedColumn])
                                 :
        parse_log (ParseLog)     :
        rows (Optional[Rows])    : Specify rows of metadata data corresponding to an
                                   identifier if collection_type is sample_sheet
    """

    elements: list[ParsedWorkbookElement]
    extra_columns: list[ParsedColumn]
    parse_log: ParseLog
    rows: Rows | None  # Specify rows of metadata data corresponding to an identifier if collection_type is sample_sheet
