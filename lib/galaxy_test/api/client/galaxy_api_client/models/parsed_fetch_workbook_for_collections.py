from dataclasses import dataclass

from .collection_type import CollectionType
from .parse_log import ParseLog
from .parsed_column import ParsedColumn
from .rows import Rows
from .workbook_type import WorkbookType

__all__ = ["ParsedFetchWorkbookForCollections"]


@dataclass
class ParsedFetchWorkbookForCollections:
    """
    ParsedFetchWorkbookForCollections dataclass.

    Args:
        collection_type (Optional[CollectionType])
                                 : The type of the collection, can be `list`, `paired`, or
                                   define subcollections using `:` as separator like
                                   `list:paired` or `list:list`.
        columns (List[ParsedColumn])
                                 :
        parse_log (ParseLog)     :
        rows (Optional[Rows])    : Specify rows of metadata data corresponding to an
                                   identifier if collection_type is sample_sheet
        workbook_type (Optional[WorkbookType])
                                 :
    """

    collection_type: (
        CollectionType | None
    )  # The type of the collection, can be `list`, `paired`, or define subcollections using `:` as separator like `list:paired` or `list:list`.
    columns: list[ParsedColumn]
    parse_log: ParseLog
    rows: Rows | None  # Specify rows of metadata data corresponding to an identifier if collection_type is sample_sheet
    workbook_type: WorkbookType | None = "datasets"
