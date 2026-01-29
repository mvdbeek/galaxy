from dataclasses import dataclass
from datetime import datetime

from .tool_format import ToolFormat
from .tool_id import ToolId
from .user_tool_source_output import UserToolSourceOutput

__all__ = ["UnprivilegedToolResponse"]


@dataclass
class UnprivilegedToolResponse:
    """
    UnprivilegedToolResponse dataclass.

    Args:
        active (bool)            :
        create_time (datetime)   :
        hidden (bool)            :
        id_ (str)                :
        representation (UserToolSourceOutput)
                                 :
        tool_format (Optional[ToolFormat])
                                 :
        tool_id (Optional[ToolId]): The unique name of the tool associated with this step.
        uuid_ (str)              :
    """

    active: bool
    create_time: datetime
    hidden: bool
    id_: str
    representation: UserToolSourceOutput
    tool_format: ToolFormat | None
    tool_id: ToolId | None  # The unique name of the tool associated with this step.
    uuid_: str
