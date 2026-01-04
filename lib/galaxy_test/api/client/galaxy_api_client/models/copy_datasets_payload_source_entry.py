from dataclasses import dataclass

__all__ = ["CopyDatasetsPayloadSourceEntry"]


@dataclass
class CopyDatasetsPayloadSourceEntry:
    """
    CopyDatasetsPayloadSourceEntry dataclass.

    Args:
        id_ (str)                :
        type_ (str)              :
    """

    id_: str
    type_: str
