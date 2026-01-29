from dataclasses import dataclass

from .requirement import Requirement
from .tags import Tags
from .title_default import TitleDefault
from .tour_step import TourStep

__all__ = ["TourDetails"]


@dataclass
class TourDetails:
    """
    TourDetails dataclass.

    Args:
        description (str)        : Tour description
        name (str)               : Name of tour
        requirements (List[Requirement])
                                 : Requirements to run the tour.
        steps (List[TourStep])   : Tour steps
        tags (Tags)              : Topic topic tags
        title_default (Optional[TitleDefault])
                                 : Default title for each step
    """

    description: str  # Tour description
    name: str  # Name of tour
    requirements: list[Requirement]  # Requirements to run the tour.
    steps: list[TourStep]  # Tour steps
    tags: Tags  # Topic topic tags
    title_default: TitleDefault | None = None  # Default title for each step
