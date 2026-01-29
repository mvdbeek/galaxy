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

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "href": "href",
            "target": "target",
            "text": "text",
        }
        key_transform_with_dump = {
            "href": "href",
            "target": "target",
            "text": "text",
        }
