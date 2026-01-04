from dataclasses import dataclass

from .elements import Elements

__all__ = ["CompositeItems"]


@dataclass
class CompositeItems:
    """
    CompositeItems dataclass.

    Args:
        elements (Elements)      :
    """

    elements: Elements
