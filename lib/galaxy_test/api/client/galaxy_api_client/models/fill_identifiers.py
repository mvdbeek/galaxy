from dataclasses import dataclass

__all__ = ["FillIdentifiers"]


@dataclass
class FillIdentifiers:
    """
    FillIdentifiers dataclass

    Args:
        deduplication_index_from (int | None)
                                 :
        deduplication_pattern (str | None)
                                 :
        fill_inner_list_identifiers (bool | None)
                                 :
    """

    deduplication_index_from: int | None = 1
    deduplication_pattern: str | None = "_{#}"
    fill_inner_list_identifiers: bool | None = False

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "deduplication_index_from": "deduplication_index_from",
            "deduplication_pattern": "deduplication_pattern",
            "fill_inner_list_identifiers": "fill_inner_list_identifiers",
        }
        key_transform_with_dump = {
            "deduplication_index_from": "deduplication_index_from",
            "deduplication_pattern": "deduplication_pattern",
            "fill_inner_list_identifiers": "fill_inner_list_identifiers",
        }
