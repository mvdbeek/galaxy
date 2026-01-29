from dataclasses import dataclass

from .parsed_column import ParsedColumn
from .parsed_workbook_element import ParsedWorkbookElement
from .parsed_workbook_for_collection_parse_log import ParsedWorkbookForCollectionParseLog
from .parsed_workbook_for_collection_rows import ParsedWorkbookForCollectionRows

__all__ = ["ParsedWorkbookForCollection"]


@dataclass
class ParsedWorkbookForCollection:
    """
    ParsedWorkbookForCollection dataclass

    Args:
        elements (List[ParsedWorkbookElement])
                                 :
        extra_columns (List[ParsedColumn])
                                 :
        parse_log (ParsedWorkbookForCollectionParseLog)
                                 :
        rows (ParsedWorkbookForCollectionRows)
                                 :
    """

    elements: list[ParsedWorkbookElement]
    extra_columns: list[ParsedColumn]
    parse_log: ParsedWorkbookForCollectionParseLog
    rows: ParsedWorkbookForCollectionRows

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "elements": "elements",
            "extra_columns": "extra_columns",
            "parse_log": "parse_log",
            "rows": "rows",
        }
        key_transform_with_dump = {
            "elements": "elements",
            "extra_columns": "extra_columns",
            "parse_log": "parse_log",
            "rows": "rows",
        }
