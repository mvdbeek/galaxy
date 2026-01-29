from dataclasses import dataclass

from .update_page_payload_annotation import UpdatePagePayloadAnnotation

__all__ = ["UpdatePagePayload"]


@dataclass
class UpdatePagePayload:
    """
    UpdatePagePayload dataclass

    Args:
        slug (str)               : The identifying slug for the page URL, must be unique.
        title (str)              : The name of the page.
        annotation (UpdatePagePayloadAnnotation | None)
                                 : Annotation that will be attached to the page.
    """

    slug: str  # The identifying slug for the page URL, must be unique.
    title: str  # The name of the page.
    annotation: UpdatePagePayloadAnnotation | None = None  # Annotation that will be attached to the page.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "annotation": "annotation",
            "slug": "slug",
            "title": "title",
        }
        key_transform_with_dump = {
            "annotation": "annotation",
            "slug": "slug",
            "title": "title",
        }
