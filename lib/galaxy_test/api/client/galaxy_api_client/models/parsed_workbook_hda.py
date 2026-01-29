from dataclasses import dataclass

__all__ = ["ParsedWorkbookHda"]


@dataclass
class ParsedWorkbookHda:
    """
    ParsedWorkbookHda dataclass

    Args:
        id_ (str)                : Maps from 'id'
        model_class (str | None) :
    """

    id_: str  # Maps from 'id'
    model_class: str | None = "HistoryDatasetAssociation"

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "id": "id_",
            "model_class": "model_class",
        }
        key_transform_with_dump = {
            "id_": "id",
            "model_class": "model_class",
        }
