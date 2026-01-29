from enum import Enum, unique

__all__ = ["Format_"]


@unique
class Format_(str, Enum):
    """
    Format_ Enum

    Args:
        restructuredtext (str)   : Value for RESTRUCTUREDTEXT
        plain_text (str)         : Value for PLAIN_TEXT
        markdown (str)           : Value for MARKDOWN
    """

    RESTRUCTUREDTEXT = "restructuredtext"
    PLAIN_TEXT = "plain_text"
    MARKDOWN = "markdown"
