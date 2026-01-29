from dataclasses import dataclass

from .create_page_payload_annotation import CreatePagePayloadAnnotation
from .create_page_payload_content import CreatePagePayloadContent
from .create_page_payload_invocation_id import CreatePagePayloadInvocationId
from .page_content_format import PageContentFormat

__all__ = ["CreatePagePayload"]


@dataclass
class CreatePagePayload:
    """
    CreatePagePayload dataclass

    Args:
        slug (str)               : The identifying slug for the page URL, must be unique.
        title (str)              : The name of the page.
        annotation (CreatePagePayloadAnnotation | None)
                                 : Annotation that will be attached to the page.
        content (CreatePagePayloadContent | None)
                                 : Text contents of the last page revision with embedded
                                   directives expanded (type dependent on content_format).
        content_format (PageContentFormat | None)
                                 :
        invocation_id (CreatePagePayloadInvocationId | None)
                                 : Encoded ID used by workflow generated reports.
    """

    slug: str  # The identifying slug for the page URL, must be unique.
    title: str  # The name of the page.
    annotation: CreatePagePayloadAnnotation | None = None  # Annotation that will be attached to the page.
    content: CreatePagePayloadContent | None = (
        ""  # Text contents of the last page revision with embedded directives expanded (type dependent on content_format).
    )
    content_format: PageContentFormat | None = None
    invocation_id: CreatePagePayloadInvocationId | None = None  # Encoded ID used by workflow generated reports.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "annotation": "annotation",
            "content": "content",
            "content_format": "content_format",
            "invocation_id": "invocation_id",
            "slug": "slug",
            "title": "title",
        }
        key_transform_with_dump = {
            "annotation": "annotation",
            "content": "content",
            "content_format": "content_format",
            "invocation_id": "invocation_id",
            "slug": "slug",
            "title": "title",
        }
