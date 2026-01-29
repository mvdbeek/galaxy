from dataclasses import dataclass

__all__ = ["ParsedWorkbookHda"]


@dataclass
class ParsedWorkbookHda:
    """
    ParsedWorkbookHda dataclass.

    Args:
        id_ (str)                :
        model_class (Optional[str])
                                 :
    """

    id_: str
    model_class: str | None = "HistoryDatasetAssociation"
