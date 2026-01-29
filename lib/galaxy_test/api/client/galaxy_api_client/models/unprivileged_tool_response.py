from dataclasses import dataclass
from datetime import datetime

from .unprivileged_tool_response_tool_format import UnprivilegedToolResponseToolFormat
from .unprivileged_tool_response_tool_id import UnprivilegedToolResponseToolId
from .user_tool_source_output import UserToolSourceOutput

__all__ = ["UnprivilegedToolResponse"]


@dataclass
class UnprivilegedToolResponse:
    """
    UnprivilegedToolResponse dataclass

    Args:
        active (bool)            :
        create_time (datetime)   :
        hidden (bool)            :
        id_ (str)                : Maps from 'id'
        representation (UserToolSourceOutput)
                                 :
        tool_format (UnprivilegedToolResponseToolFormat)
                                 :
        tool_id (UnprivilegedToolResponseToolId)
                                 :
        uuid_ (str)              : Maps from 'uuid'
    """

    active: bool
    create_time: datetime
    hidden: bool
    id_: str  # Maps from 'id'
    representation: UserToolSourceOutput
    tool_format: UnprivilegedToolResponseToolFormat
    tool_id: UnprivilegedToolResponseToolId
    uuid_: str  # Maps from 'uuid'

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "active": "active",
            "create_time": "create_time",
            "hidden": "hidden",
            "id": "id_",
            "representation": "representation",
            "tool_format": "tool_format",
            "tool_id": "tool_id",
            "uuid": "uuid_",
        }
        key_transform_with_dump = {
            "active": "active",
            "create_time": "create_time",
            "hidden": "hidden",
            "id_": "id",
            "representation": "representation",
            "tool_format": "tool_format",
            "tool_id": "tool_id",
            "uuid_": "uuid",
        }
