from dataclasses import dataclass

from .parsed_column import ParsedColumn

__all__ = ["InferredCollectionTypeLogEntry"]


@dataclass
class InferredCollectionTypeLogEntry:
    """
    InferredCollectionTypeLogEntry dataclass

    Args:
        from_columns (List[ParsedColumn])
                                 :
        message (str)            :
    """

    from_columns: list[ParsedColumn]
    message: str

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "from_columns": "from_columns",
            "message": "message",
        }
        key_transform_with_dump = {
            "from_columns": "from_columns",
            "message": "message",
        }
