from dataclasses import dataclass

from .format_ import Format_

__all__ = ["HelpContent"]


@dataclass
class HelpContent:
    """
    HelpContent dataclass.

    Args:
        content (str)            :
        format_ (Format_)        : The short name for the output datatype.
    """

    content: str
    format_: Format_  # The short name for the output datatype.
