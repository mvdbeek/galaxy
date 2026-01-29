from dataclasses import dataclass

__all__ = ["ParsedWorkbookCollection"]


@dataclass
class ParsedWorkbookCollection:
    """
    ParsedWorkbookCollection dataclass.

    Args:
        id_ (str)                :
        model_class (Optional[str])
                                 :
    """

    id_: str
    model_class: str | None = "DatasetCollection"
