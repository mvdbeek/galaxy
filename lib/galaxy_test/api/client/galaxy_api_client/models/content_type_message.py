from dataclasses import dataclass

__all__ = ["ContentTypeMessage"]


@dataclass
class ContentTypeMessage:
    """
    ContentTypeMessage dataclass

    Args:
        content_type (str)       :
        message (str)            :
    """

    content_type: str
    message: str

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "content_type": "content_type",
            "message": "message",
        }
        key_transform_with_dump = {
            "content_type": "content_type",
            "message": "message",
        }
