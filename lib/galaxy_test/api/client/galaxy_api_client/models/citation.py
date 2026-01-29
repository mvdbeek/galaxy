from dataclasses import dataclass

__all__ = ["Citation"]


@dataclass
class Citation:
    """
    Citation dataclass.

    Args:
        content (str)            :
        type_ (str)              :
    """

    content: str
    type_: str
