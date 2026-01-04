from typing import TypeAlias

from .dynamic_tool_create_payload import DynamicToolCreatePayload
from .path_based_dynamic_tool_create_payload import PathBasedDynamicToolCreatePayload

__all__ = ["DynamicToolsCreateRequestBody2"]

DynamicToolsCreateRequestBody2: TypeAlias = DynamicToolCreatePayload | PathBasedDynamicToolCreatePayload
