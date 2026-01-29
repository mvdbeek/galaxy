from dataclasses import dataclass

from .requirement import Requirement
from .tags import Tags

__all__ = ["Tour"]


@dataclass
class Tour:
    """
    Tour dataclass.

    Args:
        description (str)        : Tour description
        id_ (str)                : Tour identifier
        name (str)               : Name of tour
        requirements (List[Requirement])
                                 : Requirements to run the tour.
        tags (Tags)              : Topic topic tags
    """

    description: str  # Tour description
    id_: str  # Tour identifier
    name: str  # Name of tour
    requirements: list[Requirement]  # Requirements to run the tour.
    tags: Tags  # Topic topic tags
