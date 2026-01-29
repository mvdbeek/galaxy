from typing import TypeAlias

from .group_user_response import GroupUserResponse

__all__ = ["GroupUserListResponse"]

GroupUserListResponse: TypeAlias = list[GroupUserResponse]
