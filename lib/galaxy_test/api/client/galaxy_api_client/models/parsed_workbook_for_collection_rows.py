from typing import TypeAlias

from .parsed_workbook_for_collection_rows_item import ParsedWorkbookForCollectionRowsItem

__all__ = ["ParsedWorkbookForCollectionRows"]

ParsedWorkbookForCollectionRows: TypeAlias = list[ParsedWorkbookForCollectionRowsItem]
