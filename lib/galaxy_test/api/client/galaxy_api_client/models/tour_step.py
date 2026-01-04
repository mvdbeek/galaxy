from dataclasses import dataclass

from .content import Content
from .element import Element
from .orphan import Orphan
from .placement import Placement
from .postclick import Postclick
from .preclick import Preclick
from .textinsert import Textinsert
from .title import Title

__all__ = ["TourStep"]


@dataclass
class TourStep:
    """
    TourStep dataclass.

    Args:
        content (Optional[Content])
                                 : Text contents of the last page revision with embedded
                                   directives expanded (type dependent on content_format).
        element (Optional[Element])
                                 : CSS selector for the element to be described/clicked
        orphan (Optional[Orphan]): If true, the step is an orphan step
        placement (Optional[Placement])
                                 : Placement of the text box relative to the selected
                                   element
        postclick (Optional[Postclick])
                                 : Elements that receive a click() event after the step is
                                   shown
        preclick (Optional[Preclick])
                                 : Elements that receive a click() event before the step is
                                   shown
        textinsert (Optional[Textinsert])
                                 : Text to insert if element is a text box (e.g. tool search
                                   or upload)
        title (Optional[Title])  : The name of the visualization.
    """

    content: Content | None = (
        ""  # Text contents of the last page revision with embedded directives expanded (type dependent on content_format).
    )
    element: Element | None = None  # CSS selector for the element to be described/clicked
    orphan: Orphan | None = None  # If true, the step is an orphan step
    placement: Placement | None = None  # Placement of the text box relative to the selected element
    postclick: Postclick | None = None  # Elements that receive a click() event after the step is shown
    preclick: Preclick | None = None  # Elements that receive a click() event before the step is shown
    textinsert: Textinsert | None = None  # Text to insert if element is a text box (e.g. tool search or upload)
    title: Title | None = "Untitled Visualization"  # The name of the visualization.
