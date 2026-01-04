from dataclasses import dataclass

from .link import Link

__all__ = ["DisplayApplication"]


@dataclass
class DisplayApplication:
    """
    DisplayApplication dataclass.

    Args:
        filename (str)           :
        id_ (str)                :
        links (List[Link])       :
        name (str)               :
        version (str)            :
    """

    filename: str
    id_: str
    links: list[Link]
    name: str
    version: str
