from typing import TypeAlias

from .installed_repository_tool_shed_status import InstalledRepositoryToolShedStatus

__all__ = ["ToolShedStatus"]

ToolShedStatus: TypeAlias = InstalledRepositoryToolShedStatus | None
