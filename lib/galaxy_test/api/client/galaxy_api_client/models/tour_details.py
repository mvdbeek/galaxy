from dataclasses import dataclass

from .requirement import Requirement
from .tour_details_title_default import TourDetailsTitleDefault
from .tour_step import TourStep

__all__ = ["TourDetails"]


@dataclass
class TourDetails:
    """
    TourDetails dataclass

    Args:
        description (str)        : Tour description
        name (str)               : Name of tour
        requirements (List[Requirement])
                                 : Requirements to run the tour.
        steps (List[TourStep])   : Tour steps
        tags (List[str])         : Topic topic tags
        title_default (TourDetailsTitleDefault | None)
                                 : Default title for each step
    """

    description: str  # Tour description
    name: str  # Name of tour
    requirements: list[Requirement]  # Requirements to run the tour.
    steps: list[TourStep]  # Tour steps
    tags: list[str]  # Topic topic tags
    title_default: TourDetailsTitleDefault | None = None  # Default title for each step

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "description": "description",
            "name": "name",
            "requirements": "requirements",
            "steps": "steps",
            "tags": "tags",
            "title_default": "title_default",
        }
        key_transform_with_dump = {
            "description": "description",
            "name": "name",
            "requirements": "requirements",
            "steps": "steps",
            "tags": "tags",
            "title_default": "title_default",
        }
