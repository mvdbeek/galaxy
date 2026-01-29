from dataclasses import dataclass

__all__ = ["Hyperlink"]


@dataclass
class Hyperlink:
    """
    Represents some text with an Hyperlink.

    Args:
        href (str)               : The URL of the linked document.
        target (str)             : Specifies where to open the linked document.
        text (str)               : The text placeholder for the link.
    """

    href: str  # The URL of the linked document.
    target: str  # Specifies where to open the linked document.
    text: str  # The text placeholder for the link.
