from dataclasses import dataclass

from .hyperlink import Hyperlink

__all__ = ["DisplayApp"]


@dataclass
class DisplayApp:
    """
    Basic linked information about an application that can display certain datatypes.

    Args:
        label (str)              : The label or title of the Display Application.
        links (List[Hyperlink])  : The collection of link details for this Display
                                   Application.
    """

    label: str  # The label or title of the Display Application.
    links: list[Hyperlink]  # The collection of link details for this Display Application.
