from dataclasses import dataclass

from .parsed_column import ParsedColumn
from .parsed_fetch_workbook_for_collections_collection_type import ParsedFetchWorkbookForCollectionsCollectionType
from .parsed_fetch_workbook_for_collections_parse_log import ParsedFetchWorkbookForCollectionsParseLog
from .parsed_fetch_workbook_for_collections_rows import ParsedFetchWorkbookForCollectionsRows
from .parsed_fetch_workbook_for_collections_workbook_type import ParsedFetchWorkbookForCollectionsWorkbookType

__all__ = ["ParsedFetchWorkbookForCollections"]


@dataclass
class ParsedFetchWorkbookForCollections:
    """
    ParsedFetchWorkbookForCollections dataclass

    Args:
        collection_type (ParsedFetchWorkbookForCollectionsCollectionType)
                                 :
        columns (List[ParsedColumn])
                                 :
        parse_log (ParsedFetchWorkbookForCollectionsParseLog)
                                 :
        rows (ParsedFetchWorkbookForCollectionsRows)
                                 :
        workbook_type (ParsedFetchWorkbookForCollectionsWorkbookType | None)
                                 :
    """

    collection_type: ParsedFetchWorkbookForCollectionsCollectionType
    columns: list[ParsedColumn]
    parse_log: ParsedFetchWorkbookForCollectionsParseLog
    rows: ParsedFetchWorkbookForCollectionsRows
    workbook_type: ParsedFetchWorkbookForCollectionsWorkbookType | None = "collection"

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "collection_type": "collection_type",
            "columns": "columns",
            "parse_log": "parse_log",
            "rows": "rows",
            "workbook_type": "workbook_type",
        }
        key_transform_with_dump = {
            "collection_type": "collection_type",
            "columns": "columns",
            "parse_log": "parse_log",
            "rows": "rows",
            "workbook_type": "workbook_type",
        }
