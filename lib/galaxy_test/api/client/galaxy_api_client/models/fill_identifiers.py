from dataclasses import dataclass

__all__ = ["FillIdentifiers"]


@dataclass
class FillIdentifiers:
    """
    FillIdentifiers dataclass.

    Args:
        deduplication_index_from (Optional[int])
                                 :
        deduplication_pattern (Optional[str])
                                 :
        fill_inner_list_identifiers (Optional[bool])
                                 :
    """

    deduplication_index_from: int | None = 1
    deduplication_pattern: str | None = "_{#}"
    fill_inner_list_identifiers: bool | None = False
