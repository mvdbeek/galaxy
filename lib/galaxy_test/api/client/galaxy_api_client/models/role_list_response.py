from typing import TypeAlias

from .role_model_response import RoleModelResponse

__all__ = ["RoleListResponse"]

RoleListResponse: TypeAlias = list[RoleModelResponse]
