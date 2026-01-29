from typing import TypeAlias

from .parsed_workbook_rows_item import ParsedWorkbookRowsItem

__all__ = ["ParsedWorkbookRows"]

ParsedWorkbookRows: TypeAlias = list[ParsedWorkbookRowsItem]
