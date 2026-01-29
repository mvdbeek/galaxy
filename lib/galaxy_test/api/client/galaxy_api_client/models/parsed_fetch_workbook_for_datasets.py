from dataclasses import dataclass

from .parsed_column import ParsedColumn
from .parsed_fetch_workbook_for_datasets_parse_log import ParsedFetchWorkbookForDatasetsParseLog
from .parsed_fetch_workbook_for_datasets_rows import ParsedFetchWorkbookForDatasetsRows
from .parsed_fetch_workbook_for_datasets_workbook_type import ParsedFetchWorkbookForDatasetsWorkbookType

__all__ = ["ParsedFetchWorkbookForDatasets"]


@dataclass
class ParsedFetchWorkbookForDatasets:
    """
    ParsedFetchWorkbookForDatasets dataclass

    Args:
        columns (List[ParsedColumn])
                                 :
        parse_log (ParsedFetchWorkbookForDatasetsParseLog)
                                 :
        rows (ParsedFetchWorkbookForDatasetsRows)
                                 :
        workbook_type (ParsedFetchWorkbookForDatasetsWorkbookType | None)
                                 :
    """

    columns: list[ParsedColumn]
    parse_log: ParsedFetchWorkbookForDatasetsParseLog
    rows: ParsedFetchWorkbookForDatasetsRows
    workbook_type: ParsedFetchWorkbookForDatasetsWorkbookType | None = "datasets"

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "columns": "columns",
            "parse_log": "parse_log",
            "rows": "rows",
            "workbook_type": "workbook_type",
        }
        key_transform_with_dump = {
            "columns": "columns",
            "parse_log": "parse_log",
            "rows": "rows",
            "workbook_type": "workbook_type",
        }
