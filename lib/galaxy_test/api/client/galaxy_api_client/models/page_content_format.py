from enum import Enum, unique

__all__ = ["PageContentFormat"]


@unique
class PageContentFormat(str, Enum):
    """
    PageContentFormat Enum

    Args:
        markdown (str)           : Value for MARKDOWN
        html (str)               : Value for HTML
    """

    MARKDOWN = "markdown"
    HTML = "html"
