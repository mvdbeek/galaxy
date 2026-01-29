from dataclasses import dataclass

from .parsed_column import ParsedColumn

__all__ = ["InferredCollectionTypeLogEntry"]


@dataclass
class InferredCollectionTypeLogEntry:
    """
    InferredCollectionTypeLogEntry dataclass.

    Args:
        from_columns (List[ParsedColumn])
                                 :
        message (str)            :
    """

    from_columns: list[ParsedColumn]
    message: str
