from dataclasses import dataclass

from .annotation import Annotation
from .content import Content
from .invocation_id import InvocationId
from .page_content_format import PageContentFormat

__all__ = ["CreatePagePayload"]


@dataclass
class CreatePagePayload:
    """
    CreatePagePayload dataclass.

    Args:
        slug (str)               : The identifying slug for the page URL, must be unique.
        title (str)              : The name of the page.
        annotation (Optional[Annotation])
                                 : The annotation of this Visualization.
        content (Optional[Content])
                                 : Text contents of the last page revision with embedded
                                   directives expanded (type dependent on content_format).
        content_format (Optional[PageContentFormat])
                                 :
        invocation_id (Optional[InvocationId])
                                 : Encoded ID used by workflow generated reports.
    """

    slug: str  # The identifying slug for the page URL, must be unique.
    title: str  # The name of the page.
    annotation: Annotation | None = None  # The annotation of this Visualization.
    content: Content | None = (
        ""  # Text contents of the last page revision with embedded directives expanded (type dependent on content_format).
    )
    content_format: PageContentFormat | None = None
    invocation_id: InvocationId | None = None  # Encoded ID used by workflow generated reports.
