from dataclasses import dataclass

from .active import Active
from .hidden import Hidden
from .user_tool_source_input import UserToolSourceInput

__all__ = ["DynamicUnprivilegedToolCreatePayload"]


@dataclass
class DynamicUnprivilegedToolCreatePayload:
    """
    DynamicUnprivilegedToolCreatePayload dataclass.

    Args:
        representation (UserToolSourceInput)
                                 :
        active (Optional[Active]): User is active
        hidden (Optional[Hidden]): If true, the output will not be shown in the history.
        src (Optional[str])      :
    """

    representation: UserToolSourceInput
    active: Active | None = True  # User is active
    hidden: Hidden | None = False  # If true, the output will not be shown in the history.
    src: str | None = "representation"
