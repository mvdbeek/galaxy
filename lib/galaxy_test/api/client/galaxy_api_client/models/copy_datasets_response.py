from dataclasses import dataclass

__all__ = ["CopyDatasetsResponse"]


@dataclass
class CopyDatasetsResponse:
    """
    CopyDatasetsResponse dataclass

    Args:
        history_ids (List[str])  :
    """

    history_ids: list[str]

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "history_ids": "history_ids",
        }
        key_transform_with_dump = {
            "history_ids": "history_ids",
        }
