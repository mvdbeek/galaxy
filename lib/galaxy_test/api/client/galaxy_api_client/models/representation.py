from typing import TypeAlias

from .admin_tool_source import AdminToolSource
from .user_tool_source_input import UserToolSourceInput

__all__ = ["Representation"]

Representation: TypeAlias = AdminToolSource | UserToolSourceInput
