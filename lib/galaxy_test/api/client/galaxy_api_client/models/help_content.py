from dataclasses import dataclass

from .format_ import Format_

__all__ = ["HelpContent"]


@dataclass
class HelpContent:
    """
    HelpContent dataclass

    Args:
        content (str)            :
        format_ (Format_)        : Maps from 'format'
    """

    content: str
    format_: Format_  # Maps from 'format'

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "content": "content",
            "format": "format_",
        }
        key_transform_with_dump = {
            "content": "content",
            "format_": "format",
        }
