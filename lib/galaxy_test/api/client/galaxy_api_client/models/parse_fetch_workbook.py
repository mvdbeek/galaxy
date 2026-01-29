from dataclasses import dataclass

from .parse_fetch_workbook_fill_identifiers import ParseFetchWorkbookFillIdentifiers

__all__ = ["ParseFetchWorkbook"]


@dataclass
class ParseFetchWorkbook:
    """
    ParseFetchWorkbook dataclass

    Args:
        content (str)            : The workbook content (the contents of the xlsx file) that
                                   have been base64 encoded.
        fill_identifiers (ParseFetchWorkbookFillIdentifiers | None)
                                 :
    """

    content: str  # The workbook content (the contents of the xlsx file) that have been base64 encoded.
    fill_identifiers: ParseFetchWorkbookFillIdentifiers | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "content": "content",
            "fill_identifiers": "fill_identifiers",
        }
        key_transform_with_dump = {
            "content": "content",
            "fill_identifiers": "fill_identifiers",
        }
