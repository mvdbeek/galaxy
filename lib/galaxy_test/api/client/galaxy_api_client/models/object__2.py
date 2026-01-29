from typing import TypeAlias

from .parsed_workbook_collection import ParsedWorkbookCollection
from .parsed_workbook_hda import ParsedWorkbookHda

__all__ = ["Object2"]

Object2: TypeAlias = ParsedWorkbookHda | ParsedWorkbookCollection
