from dataclasses import dataclass

from .requirement import Requirement

__all__ = ["Tour"]


@dataclass
class Tour:
    """
    Tour dataclass

    Args:
        description (str)        : Tour description
        id_ (str)                : Tour identifier (maps from 'id')
        name (str)               : Name of tour
        requirements (List[Requirement])
                                 : Requirements to run the tour.
        tags (List[str])         : Topic topic tags
    """

    description: str  # Tour description
    id_: str  # Tour identifier (maps from 'id')
    name: str  # Name of tour
    requirements: list[Requirement]  # Requirements to run the tour.
    tags: list[str]  # Topic topic tags

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "description": "description",
            "id": "id_",
            "name": "name",
            "requirements": "requirements",
            "tags": "tags",
        }
        key_transform_with_dump = {
            "description": "description",
            "id_": "id",
            "name": "name",
            "requirements": "requirements",
            "tags": "tags",
        }
