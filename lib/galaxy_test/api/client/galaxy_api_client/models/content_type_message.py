from dataclasses import dataclass

__all__ = ["ContentTypeMessage"]


@dataclass
class ContentTypeMessage:
    """
    ContentTypeMessage dataclass.

    Args:
        content_type (str)       :
        message (str)            :
    """

    content_type: str
    message: str
