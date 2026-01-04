from dataclasses import dataclass

from .active import Active
from .hidden import Hidden
from .representation import Representation

__all__ = ["DynamicToolCreatePayload"]


@dataclass
class DynamicToolCreatePayload:
    """
    DynamicToolCreatePayload dataclass.

    Args:
        representation (Representation)
                                 :
        active (Optional[Active]): User is active
        hidden (Optional[Hidden]): If true, the output will not be shown in the history.
        src (Optional[str])      :
    """

    representation: Representation
    active: Active | None = True  # User is active
    hidden: Hidden | None = False  # If true, the output will not be shown in the history.
    src: str | None = "representation"
