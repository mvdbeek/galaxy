from dataclasses import dataclass

from .csv_dialect import CsvDialect

__all__ = ["CsvDialectInferenceMessage"]


@dataclass
class CsvDialectInferenceMessage:
    """
    CsvDialectInferenceMessage dataclass.

    Args:
        dialect (CsvDialect)     :
        message (str)            :
    """

    dialect: CsvDialect
    message: str
