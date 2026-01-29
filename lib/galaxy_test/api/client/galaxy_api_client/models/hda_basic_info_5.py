from dataclasses import dataclass

__all__ = ["HdaBasicInfo5"]


@dataclass
class HdaBasicInfo5:
    """
    HdaBasicInfo5 dataclass.

    Args:
        id_ (str)                :
        name (str)               :
    """

    id_: str
    name: str
