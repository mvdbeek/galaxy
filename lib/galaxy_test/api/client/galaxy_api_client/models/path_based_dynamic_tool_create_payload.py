from dataclasses import dataclass

from .active import Active
from .hidden import Hidden
from .tool_directory import ToolDirectory

__all__ = ["PathBasedDynamicToolCreatePayload"]


@dataclass
class PathBasedDynamicToolCreatePayload:
    """
    PathBasedDynamicToolCreatePayload dataclass.

    Args:
        path (str)               :
        src (str)                :
        active (Optional[Active]): User is active
        hidden (Optional[Hidden]): If true, the output will not be shown in the history.
        tool_directory (Optional[ToolDirectory])
                                 :
    """

    path: str
    src: str
    active: Active | None = True  # User is active
    hidden: Hidden | None = False  # If true, the output will not be shown in the history.
    tool_directory: ToolDirectory | None = None
