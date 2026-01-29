from dataclasses import dataclass

from .fill_identifiers import FillIdentifiers

__all__ = ["ParseFetchWorkbook"]


@dataclass
class ParseFetchWorkbook:
    """
    ParseFetchWorkbook dataclass.

    Args:
        content (str)            : The workbook content (the contents of the xlsx file) that
                                   have been base64 encoded.
        fill_identifiers (Optional[FillIdentifiers])
                                 :
    """

    content: str  # The workbook content (the contents of the xlsx file) that have been base64 encoded.
    fill_identifiers: FillIdentifiers | None = None
