from dataclasses import dataclass

from .tour_step_content import TourStepContent
from .tour_step_element import TourStepElement
from .tour_step_orphan import TourStepOrphan
from .tour_step_placement import TourStepPlacement
from .tour_step_postclick import TourStepPostclick
from .tour_step_preclick import TourStepPreclick
from .tour_step_textinsert import TourStepTextinsert
from .tour_step_title import TourStepTitle

__all__ = ["TourStep"]


@dataclass
class TourStep:
    """
    TourStep dataclass

    Args:
        content (TourStepContent | None)
                                 : Text shown to the user
        element (TourStepElement | None)
                                 : CSS selector for the element to be described/clicked
        orphan (TourStepOrphan | None)
                                 : If true, the step is an orphan step
        placement (TourStepPlacement | None)
                                 : Placement of the text box relative to the selected
                                   element
        postclick (TourStepPostclick | None)
                                 : Elements that receive a click() event after the step is
                                   shown
        preclick (TourStepPreclick | None)
                                 : Elements that receive a click() event before the step is
                                   shown
        textinsert (TourStepTextinsert | None)
                                 : Text to insert if element is a text box (e.g. tool search
                                   or upload)
        title (TourStepTitle | None)
                                 : Title displayed in the header of the step container
    """

    content: TourStepContent | None = None  # Text shown to the user
    element: TourStepElement | None = None  # CSS selector for the element to be described/clicked
    orphan: TourStepOrphan | None = None  # If true, the step is an orphan step
    placement: TourStepPlacement | None = None  # Placement of the text box relative to the selected element
    postclick: TourStepPostclick | None = None  # Elements that receive a click() event after the step is shown
    preclick: TourStepPreclick | None = None  # Elements that receive a click() event before the step is shown
    textinsert: TourStepTextinsert | None = None  # Text to insert if element is a text box (e.g. tool search or upload)
    title: TourStepTitle | None = None  # Title displayed in the header of the step container

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "content": "content",
            "element": "element",
            "orphan": "orphan",
            "placement": "placement",
            "postclick": "postclick",
            "preclick": "preclick",
            "textinsert": "textinsert",
            "title": "title",
        }
        key_transform_with_dump = {
            "content": "content",
            "element": "element",
            "orphan": "orphan",
            "placement": "placement",
            "postclick": "postclick",
            "preclick": "preclick",
            "textinsert": "textinsert",
            "title": "title",
        }
