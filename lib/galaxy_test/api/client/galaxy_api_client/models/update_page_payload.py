from dataclasses import dataclass

from .annotation import Annotation

__all__ = ["UpdatePagePayload"]


@dataclass
class UpdatePagePayload:
    """
    UpdatePagePayload dataclass.

    Args:
        slug (str)               : The identifying slug for the page URL, must be unique.
        title (str)              : The name of the page.
        annotation (Optional[Annotation])
                                 : The annotation of this Visualization.
    """

    slug: str  # The identifying slug for the page URL, must be unique.
    title: str  # The name of the page.
    annotation: Annotation | None = None  # The annotation of this Visualization.
