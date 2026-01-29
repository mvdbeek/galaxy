from dataclasses import dataclass

from .parsed_column import ParsedColumn
from .parsed_workbook_parse_log import ParsedWorkbookParseLog
from .parsed_workbook_rows import ParsedWorkbookRows

__all__ = ["ParsedWorkbook"]


@dataclass
class ParsedWorkbook:
    """
    ParsedWorkbook dataclass

    Args:
        extra_columns (List[ParsedColumn])
                                 :
        parse_log (ParsedWorkbookParseLog)
                                 :
        rows (ParsedWorkbookRows):
    """

    extra_columns: list[ParsedColumn]
    parse_log: ParsedWorkbookParseLog
    rows: ParsedWorkbookRows

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "extra_columns": "extra_columns",
            "parse_log": "parse_log",
            "rows": "rows",
        }
        key_transform_with_dump = {
            "extra_columns": "extra_columns",
            "parse_log": "parse_log",
            "rows": "rows",
        }
