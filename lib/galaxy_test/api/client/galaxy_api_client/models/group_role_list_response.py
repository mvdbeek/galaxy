from typing import TypeAlias

from .group_role_response import GroupRoleResponse

__all__ = ["GroupRoleListResponse"]

GroupRoleListResponse: TypeAlias = list[GroupRoleResponse]
