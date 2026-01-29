from dataclasses import dataclass

from .csv_dialect import CsvDialect

__all__ = ["CsvDialectInferenceMessage"]


@dataclass
class CsvDialectInferenceMessage:
    """
    CsvDialectInferenceMessage dataclass

    Args:
        dialect (CsvDialect)     :
        message (str)            :
    """

    dialect: CsvDialect
    message: str

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "dialect": "dialect",
            "message": "message",
        }
        key_transform_with_dump = {
            "dialect": "dialect",
            "message": "message",
        }
